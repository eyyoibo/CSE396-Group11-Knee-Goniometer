---
title: "[M1] ESP32 PCNT Hardware Pulse Counter Driver Setup"
labels: ["module-1", "hardware", "priority-high"]
milestone: "M1-Hardware Prototype"
assignees: ["Ibrahim Halil Dogan", "Mert Canoglu"]
---

## 📌 Task Description
Configure the dedicated hardware **PCNT (Pulse Counter)** peripheral on the ESP32 microcontroller to decode quadrature A/B differential signals from the dual 5000 PPR optical/magnetic incremental rotary encoders mounted on the knee brace in 4x quadrature mode without CPU polling overhead.

## 🎯 Acceptance Criteria
- [ ] Initialize Left Knee (PCNT Unit 0) and Right Knee (PCNT Unit 1) using ESP-IDF `driver/pulse_cnt.h` API.
- [ ] Configure 4-edge triggering (EDGE_RISING / EDGE_FALLING on both channels) to verify $5000 \times 4 = 20,000$ counts per mechanical revolution ($\approx 0.018^\circ$ resolution).
- [ ] Handle hardware 16-bit counter overflow/underflow (-32,768 to +32,767) via hardware interrupt (ISR) to continuously update a 32-bit cumulative count (`int32_t`).
- [ ] Enable the hardware glitch filter (~1 µs) on PCNT inputs to suppress transient contact bounce and high-frequency noise.
- [ ] Implement `pcnt_get_counts(int32_t *left, int32_t *right)` for atomic count retrieval.

## 📋 Subtasks
- [ ] Define GPIO pin mappings in `module1_hardware_encoder/include/config.h`.
- [ ] Implement `pcnt_init_encoders()` in `module1_hardware_encoder/src/main.c`.
- [ ] Validate 20,000 counts per 360° mechanical rotation on the testbench using an oscilloscope or serial output.
