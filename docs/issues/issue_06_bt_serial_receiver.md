---
title: "[M2] Bluetooth Serial Receiver QThread and Packet Demuxer"
labels: ["module-2", "software", "priority-high"]
milestone: "M2-Desktop MVP"
assignees: ["Ibrahim Halil Dogan", "Cansu Bulut"]
---

## 📌 Task Description
Prevent PyQt6 main event loop starvation by implementing a dedicated background worker thread (`QThread`) that continuously reads, validates, and decodes 50 Hz binary telemetry packets arriving over the Bluetooth SPP virtual serial port.

## 🎯 Acceptance Criteria
- [ ] Non-blocking byte reads using `pyserial` from the selected serial port.
- [ ] Frame synchronizer: locate `0xAA 0x55` header in circular buffer and parse 28-byte packet via `shared/packet_parser.py`.
- [ ] Detect and log CRC16 checksum corruptions and sequence number gaps (packet drop rate).
- [ ] Emit Qt signal `new_packet_received(TelemetryPacket)` for every successfully validated frame.
- [ ] Handle unexpected device disconnection gracefully without crashing the UI, emitting an error signal and entering safe reconnect state.

## 📋 Subtasks
- [ ] Implement `run()` polling loop in `module2_interface_rmse/src/bluetooth_receiver.py`.
- [ ] Test 50 Hz streaming stability using the synthetic data generator.
