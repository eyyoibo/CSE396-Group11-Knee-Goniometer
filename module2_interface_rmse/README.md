# Module 2: Desktop Interface & RMSE Analysis

## Overview

This module provides a responsive PyQt6 desktop application designed to acquire, visualize, and statistically analyze multi-modal joint kinematics in real time. It receives the 50 Hz Bluetooth SPP telemetry stream from the ESP32 hardware, aligns it with optical angles from the computer vision pipeline (Module 3), computes sliding-window RMSE/MAE metrics, visualizes Bland-Altman agreement curves, and exports synchronized CSV sessions.

## Core Features

- **Bluetooth SPP Acquisition:** Dedicated `QThread` serial worker that continuously receives 28-byte binary packets, validates CRC-16 checksums, and handles connection recovery.
- **High-Performance Plotting:** Utilizes `pyqtgraph` for hardware-accelerated 30–50 FPS rendering of dual angular waveforms ($\theta_{enc}$ vs $\theta_{cam}$), raw pulse counts $N(t)$, and derivative velocities $\Delta N(t)$.
- **Sliding-Window Discrepancy Engine:** Computes real-time Root Mean Square Error (RMSE) and Mean Absolute Error (MAE) over a 5-second circular buffer.
- **Bland-Altman Agreement Plot:** Calculates systematic bias ($\bar{d}$), standard deviation of differences ($SD$), and $95\%$ Limits of Agreement ($\bar{d} \pm 1.96 \cdot SD$).
- **Synchronized CSV Logging:** Writes time-aligned multi-channel session files with microsecond timestamps and validity flags.

## Architecture

```text
┌─────────────────────────────────────────┐
│              MainWindow                 │
│  ┌──────────┐  ┌──────────────────┐     │
│  │ Controls │  │ PyQtGraph        │     │
│  │ (Z/S/P)  │  │ Live Charts      │     │
│  └──────────┘  └──────────────────┘     │
│       │              ▲                  │
│       ▼              │                  │
│  ┌──────────────────────────────────┐   │
│  │   BluetoothReceiver (QThread)    │   │
│  │   Packet parsing & CRC-16 check  │   │
│  └──────────────────────────────────┘   │
│       │                                 │
│       ▼                                 │
│  ┌────────────────┐  ┌──────────────┐   │
│  │ AnalysisEngine │  │  CSVLogger   │   │
│  │ RMSE, MAE,     │  │  Disk I/O    │   │
│  │ Bland-Altman   │  │              │   │
│  └────────────────┘  └──────────────┘   │
└─────────────────────────────────────────┘
```

## Source Code Layout

| File | Responsibility |
|---|---|
| `src/main_window.py` | PyQt6 main UI window, layout, and control signal/slot bindings |
| `src/bluetooth_receiver.py` | Non-blocking background worker thread for Bluetooth SPP stream ingestion |
| `src/analysis_engine.py` | Sliding-window RMSE/MAE and post-hoc Bland-Altman statistical methods |
| `src/csv_logger.py` | Buffered CSV file writer with automatic session timestamping |

## Mathematical Formulations

### Sliding-Window Root Mean Square Error (RMSE)
$$\text{RMSE} = \sqrt{\frac{1}{N}\sum_{i=1}^{N} \left(\theta_{camera}(t_i) - \theta_{encoder}(t_i)\right)^2}$$

### Sliding-Window Mean Absolute Error (MAE)
$$\text{MAE} = \frac{1}{N}\sum_{i=1}^{N} |\theta_{camera}(t_i) - \theta_{encoder}(t_i)|$$

### Bland-Altman Analysis
* **Pairwise Differences:** $D_i = \theta_{camera}(t_i) - \theta_{encoder}(t_i)$
* **Mean Difference (Bias):** $\bar{d} = \frac{1}{N}\sum_{i=1}^{N} D_i$
* **Limits of Agreement (LoA):** $\bar{d} \pm 1.96 \cdot SD(D)$

## Installation & Launch

```bash
pip install -r requirements.txt
python -m module2_interface_rmse.src.main_window
```

## TODO Checklist

- [ ] Complete PyQt6 dark-theme UI layout in `main_window.py`
- [ ] Connect `QThread` signal `new_packet_received` to PyQtGraph curves
- [ ] Implement circular buffer for 5-second sliding window in `analysis_engine.py`
- [ ] Implement Matplotlib Bland-Altman plot export in `analysis_engine.py`
- [ ] Implement robust CSV file flushing in `csv_logger.py`
