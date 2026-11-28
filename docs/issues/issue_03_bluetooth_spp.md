---
title: "[M1] Bluetooth Classic SPP Telemetry Layer and Z/S/P State Machine"
labels: ["module-1", "software", "priority-high"]
milestone: "M1-Hardware Prototype"
assignees: ["Ibrahim Halil Dogan", "Cem Baygin"]
---

## 📌 Task Description
Implement a Bluetooth Classic Serial Port Profile (SPP / RFCOMM) server on the ESP32. Transmit 28-byte binary telemetry packets at a deterministic 50 Hz rate and process single-byte incoming ASCII commands (`Z`, `S`, `P`) from desktop and mobile hosts inside a deterministic FreeRTOS state machine.

## 🎯 Acceptance Criteria
- [ ] Initialize SPP server with advertising name `ESP32_GONIOMETER` using ESP-IDF `esp_spp_api.h` and `esp_bt_main.h`.
- [ ] Run a periodic FreeRTOS timer task at 20 ms intervals ($50\text{ Hz}$) to assemble and transmit 28-byte binary packets.
- [ ] Maintain an average transmission rate $\ge 48\text{ Hz}$ with $<1\%$ packet loss over a continuous 5-minute stress test.
- [ ] Implement ASCII command handler:
  - `'Z'`: Reset cumulative encoder offset to zero (re-calibration baseline).
  - `'S'`: Start/resume telemetry streaming (`STATE_STREAMING`).
  - `'P'`: Pause telemetry streaming (`STATE_PAUSED`).

## 📋 Subtasks
- [ ] Implement `bluetooth_spp_init()` and `send_telemetry_packet()` in `module1_hardware_encoder/src/main.c`.
- [ ] Implement CRC-16-CCITT calculation function over the first 26 payload bytes.
- [ ] Implement auto-reconnect listening loop upon client Bluetooth disconnection.
