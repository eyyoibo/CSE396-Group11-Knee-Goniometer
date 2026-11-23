# Agent Instructions — Knee Goniometer & Pose Estimation

## Repository Structure Overview

```
knee-goniometer-pose-estimation/
├── m1-firmware/           # ESP32 firmware (ESP-IDF / C)
│   ├── main/              # Application entry point and core logic
│   ├── components/        # Reusable ESP-IDF components (encoder, bluetooth, packet)
│   └── test/              # Firmware unit tests
├── m2-desktop/            # Desktop GUI application (Python / PyQt6)
│   ├── src/               # Application source code
│   ├── tests/             # pytest test suite
│   └── resources/         # UI assets, icons
├── m3-camera/             # Camera-based pose estimation (Python / MediaPipe)
│   ├── src/               # Pipeline source code
│   ├── tests/             # pytest test suite
│   └── models/            # Model configuration files
├── m4-mobile/             # Mobile application (React Native)
│   ├── src/               # App source code
│   └── __tests__/         # Jest test suite
├── shared/                # Cross-module shared utilities
│   ├── packet_parser/     # 28-byte packet format parser (Python + C + JS)
│   ├── synthetic_data/    # Test data generators
│   └── protocols/         # Protocol documentation and constants
├── docs/                  # Project documentation, reports, diagrams
├── data/                  # Collected measurement data (gitignored except examples)
└── scripts/               # Build, deploy, and utility scripts
```

## Module Navigation

### M1 — Hardware & Firmware
Entry point: `m1-firmware/main/app_main.c`
The firmware reads two quadrature encoders via GPIO interrupts, computes knee angle in degrees, and packages data into a 28-byte binary packet. This packet is transmitted over Bluetooth Classic SPP (for desktop) and BLE GATT (for mobile). Key files:
- `components/encoder/` — Quadrature encoder driver
- `components/bluetooth/` — SPP and BLE GATT server implementation
- `components/packet/` — Packet construction and CRC

### M2 — Desktop GUI
Entry point: `m2-desktop/src/main.py`
A PyQt6 application that connects to the ESP32 via Bluetooth serial port. Displays real-time angle data on a scrolling chart, allows session recording to CSV, and provides calibration controls.

### M3 — Camera Pipeline
Entry point: `m3-camera/src/main.py`
Uses OpenCV to capture video frames and MediaPipe Pose to detect body landmarks. Calculates knee flexion/extension angle from hip-knee-ankle landmark positions. Can run standalone or be embedded into the M2 desktop GUI for side-by-side comparison.

### M4 — Mobile App
Entry point: `m4-mobile/src/App.tsx`
A React Native app that connects to the ESP32 via BLE. Displays real-time angle readings and session history. Designed for clinical portability.

## Key Data Flow

```
                    ┌──────────────┐
                    │   Encoders   │
                    │  (Hardware)  │
                    └──────┬───────┘
                           │ GPIO interrupts
                    ┌──────▼───────┐
                    │    ESP32     │
                    │  (Firmware)  │
                    └──┬───────┬───┘
          Bluetooth SPP│       │BLE GATT
                 ┌─────▼──┐  ┌─▼────────┐
                 │Desktop │  │  Mobile   │
                 │  GUI   │  │   App     │
                 │ (PyQt) │  │(React N.) │
                 └────────┘  └──────────┘

      ┌────────────┐
      │   Camera   │
      └─────┬──────┘
            │ Video frames
      ┌─────▼──────┐
      │ MediaPipe  │
      │   Pose     │
      └─────┬──────┘
            │ Landmark coordinates
      ┌─────▼──────┐
      │   Angle    │
      │ Calculator │
      └────────────┘
```

Both data streams (encoder angle + camera angle) are timestamped and merged in the desktop GUI for comparison analysis.

## Development Workflow

### Branch Naming
- `feature/m1/encoder-driver` — New feature for Module 1
- `fix/m2/chart-rendering` — Bug fix for Module 2
- `docs/architecture-update` — Documentation changes
- `test/m3/angle-calculation` — Adding tests for Module 3

### Commit Message Convention
Prefix every commit with the module tag:
- `[M1] Encoder sürücüsü GPIO kesme yapılandırması eklendi`
- `[M2] Gerçek zamanlı grafik performansı iyileştirildi`
- `[M3] MediaPipe landmark tespiti doğruluğu artırıldı`
- `[M4] BLE bağlantı yönetimi düzeltildi`
- `[SHARED] Paket ayrıştırıcı CRC doğrulaması eklendi`
- `[DOCS] Mimari diyagramı güncellendi`

## Testing Strategy

| Module | Framework | Focus Areas |
|--------|-----------|-------------|
| M1 | Unity (C) + synthetic serial | Encoder reading accuracy, packet integrity, CRC validation |
| M2 | pytest | Bluetooth data parsing, CSV export, GUI state management |
| M3 | pytest | Angle calculation accuracy, landmark detection edge cases |
| M4 | Jest + React Native Testing Library | BLE connection handling, component rendering |
| Shared | pytest + Jest | Packet parser consistency across languages |

Use the synthetic data generator in `shared/synthetic_data/` to test without hardware. It produces realistic 28-byte packets with configurable angle sequences.

## Important Reminders

- Do NOT add yourself or any AI tool as a contributor to this project
- The project team is: Ibrahim Halil Dogan, Mert Canoglu, Cem Baygin
- Academic advisor: Prof. Dr. Erkan Zergeroglu
- Keep module boundaries clean — shared code goes in `shared/`
