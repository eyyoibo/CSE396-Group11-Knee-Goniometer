# Mobile UI Screen Specifications

This document outlines the user interface screens, layout requirements, data flows, and state interactions for the companion mobile application.

---

## 1. Connection Screen

### Objective
Enables scanning, discovery, and pairing with the ESP32 hardware (`ESP32_GONIOMETER`) over Bluetooth Classic SPP.

### Key UI Elements
- **Scan Button:** Initiates / terminates Bluetooth discovery.
- **Discovered Device List:** Displays device names, MAC addresses, and RSSI signal indicators.
- **Connection Status Banner:** Top status indicator (Red: Disconnected, Yellow: Connecting, Green: Connected).
- **Permissions Warning:** Prompts for Bluetooth scanning and location runtime permissions if not granted.

---

## 2. Live Dashboard Screen

### Objective
Displays high-visibility real-time angular flexion telemetry for rapid field assessment.

### Key UI Elements
- **Semicircular Dynamic Gauge (0°–150°):** Color-coded ranges:
  - $0^\circ - 30^\circ$: Red / Warning (Hyperextension / Terminal Extension)
  - $30^\circ - 120^\circ$: Green (Normal Functional Range of Motion)
  - $120^\circ - 150^\circ$: Blue (Deep Flexion)
- **Numerical Angle Readout:** Large digital display showing instantaneous angle to 1 decimal place (e.g. `87.4°`).
- **Telemetry Health Indicators:** Live sample rate display (~50 Hz) and dropped packet counter.
- **ROM Min / Max Trackers:** Displays minimum and maximum flexion angles recorded during the active session.

---

## 3. Remote Control Screen

### Objective
Dispatches single-byte calibration and session recording commands to the ESP32 firmware.

### Key UI Elements
- **Zero Calibration Button (`'Z'`):** Orange button. Requires a 1-second press-and-hold to prevent accidental triggers. Transmits `'Z'` to set current posture as $0.0^\circ$.
- **Start Recording Button (`'S'`):** Green button. Transmits `'S'` to initiate high-speed telemetry streaming and starts the session timer.
- **Pause Recording Button (`'P'`):** Red button. Transmits `'P'` to halt transmission.
- **Session Stopwatch:** Displays elapsed active capture time (`HH:MM:SS`).

---

## 4. Session History Screen

### Objective
Stores and visualizes historical recording sessions cached locally on device storage.

### Key UI Elements
- **Session List:** Chronological card list showing date, task type, duration, and peak Range of Motion (ROM).
- **Session Detail View:**
  - Angular trajectory vs. time line chart.
  - Summary metrics: Mean angle, Peak angle, ROM ($\theta_{max} - \theta_{min}$).
- **Export Action:** Exports session data in CSV format via the native OS share sheet.

---

## 5. Settings Screen

### Objective
Configures app preferences, units, connection timeouts, and storage management.

### Key UI Elements
- **Auto-Connect Toggle:** Automatically connects to the last paired device on launch.
- **Unit Selector:** Toggle between Degrees (°) and Radians (rad).
- **Storage Management:** Clear cached session logs and display local disk footprint.
