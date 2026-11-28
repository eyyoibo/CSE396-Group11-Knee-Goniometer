---
title: "[Shared] Synthetic Telemetry Data Generator for Hardware-Free Testing"
labels: ["testing", "software", "priority-high"]
milestone: "M2-Desktop MVP"
assignees: ["Cansu Bulut", "Mert Canoglu"]
---

## 📌 Task Description
Enable parallel development and automated integration testing of Module 2 (Desktop Interface) and Module 3 (Temporal Synchronization) before physical ESP32 hardware and sensor harnesses are assembled, by developing a realistic synthetic telemetry packet generator mimicking knee flexion squat patterns.

## 🎯 Acceptance Criteria
- [ ] Configurable parameters: packet frequency (50 Hz), motion cycle frequency (e.g. 2s period 0°-90° squat sinusoid), and Gaussian noise ($\sigma = 0.3^\circ$).
- [ ] Output format: Exactly matches 28-byte firmware binary protocol (`0xAA 0x55`, incremental sequence ID, timestamp ms, left/right count, left/right angle, CRC16).
- [ ] Transport interfaces: Virtual serial port (COM / pty) and local TCP server (`127.0.0.1:9000`).
- [ ] Verify that desktop dashboard launches, receives synthetic packets, plots multi-curves, and calculates sliding RMSE without physical hardware connected.

## 📋 Subtasks
- [ ] Implement `generate_angle()`, `build_packet()`, and `run_serial()` in `shared/synthetic_data_generator.py`.
- [ ] Execute automated integration test with `shared/packet_parser.py`.
