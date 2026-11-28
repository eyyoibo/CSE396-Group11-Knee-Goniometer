# Module 4: Mobile Application

## Overview

This module provides a companion cross-platform mobile application (React Native / Expo) for the wireless knee goniometer system. Connecting via Bluetooth Classic SPP to the ESP32, it enables real-time angular gauge monitoring, remote zero calibration (`Z`), start (`S`), and pause (`P`) session control, and local session review for field evaluations without requiring a laptop.

## Core Features

- **Live Dynamic Angular Gauge:** High-contrast semicircular dial displaying joint flexion angle ($0^\circ - 150^\circ$) with color-coded mobility ranges.
- **Wireless SPP Connectivity:** Bi-directional Bluetooth stream handler with automatic reconnect and packet validation.
- **Remote Hardware Control:**
  - **`'Z'` (Zero):** Zero-extension calibration command.
  - **`'S'` (Start):** Begins 50 Hz telemetry transmission and session timer.
  - **`'P'` (Pause):** Halts telemetry streaming.
- **Session Persistence:** Local session recording with timestamped CSV/JSON export.
- **Field Portability:** Enables sports trainers and evaluators to observe live metrics portably.

## Architecture & Technology Stack

* **Framework:** React Native (Expo)
* **Language:** TypeScript
* **Bluetooth Bridge:** `react-native-bluetooth-classic`
* **Vector Graphics:** `react-native-svg` (custom gauge dial)

For detailed UI screen flow and state management specifications, refer to [docs/SCREENS.md](docs/SCREENS.md).

## Installation & Setup

```bash
cd module4_mobile_app
npm install
npx expo start
```

## TODO Checklist

- [ ] Configure Android Bluetooth permissions in `app.json`
- [ ] Implement `BluetoothService.ts` with device discovery and SPP socket handling
- [ ] Connect `AngleGauge.tsx` needle rotation to incoming angle stream
- [ ] Implement remote `'Z'`, `'S'`, `'P'` command button dispatches in `ControlScreen.tsx`
- [ ] Implement local session history caching using AsyncStorage / SQLite
