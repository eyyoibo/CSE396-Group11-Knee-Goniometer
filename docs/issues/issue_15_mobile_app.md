---
title: "[M4] Mobile Companion App Development (Dial Gauge, BLE/SPP, Z/S/P Control)"
labels: ["module-4", "software", "priority-low"]
milestone: "M4-Mobile App"
assignees: ["Ibrahim Halil Dogan", "Cem Baygin"]
---

## 📌 Task Description
Develop a cross-platform React Native / Expo companion mobile application allowing coaches, physiotherapists, and athletes to monitor live knee flexion angles, receive visual biofeedback, and issue Z/S/P commands untethered in field conditions without a laptop.

## 🎯 Acceptance Criteria
- [ ] Bluetooth Classic SPP / BLE connection lifecycle management (device discovery, connect/disconnect, and drop recovery).
- [ ] Dashboard Screen: Circular animated dial gauge showing instantaneous angle (0° to 150°) with numerical readout and color thresholds.
- [ ] Control Screen:
  - 'Z' Button (Zero calibration offset command)
  - 'S' Button (Start telemetry streaming)
  - 'P' Button (Pause telemetry streaming)
- [ ] History Screen: Session duration, peak Range of Motion (ROM), and local CSV export/sharing.

## 📋 Subtasks
- [ ] Implement Bluetooth communication logic in `module4_mobile_app/src/services/BluetoothService.ts`.
- [ ] Connect SVG needle rotation and angle bindings in `module4_mobile_app/src/components/AngleGauge.tsx`.
- [ ] Validate packet decoding and UI responsiveness on a physical Android mobile device.
