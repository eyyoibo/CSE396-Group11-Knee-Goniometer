---
title: "[M1] Firmware Pulse-to-Angle Conversion and Zero Calibration"
labels: ["module-1", "software", "priority-high"]
milestone: "M1-Hardware Prototype"
assignees: ["Ibrahim Halil Dogan", "Mert Canoglu"]
---

## 📌 Task Description
Convert raw hardware pulse counts ($N(t)$) into calibrated physiological knee flexion angles ($\theta$) in firmware by applying mechanical transmission and encoder resolution scaling factors. Dynamically compute the zero offset upon receiving the 'Z' calibration command.

## 🎯 Acceptance Criteria
- [ ] Implement angle calculation formula: $\theta = (N - N_{\text{offset}}) \times \frac{360.0}{20000.0} = (N - N_{\text{offset}}) \times 0.018^\circ$.
- [ ] On `'Z'` command reception, set $N_{\text{offset}} = N_{\text{current}}$ such that immediate telemetry angle output reads $0.0^\circ$.
- [ ] Provide configurable clamping to prevent negative angles during hyperextension (bound strictly between 0.0° and 180.0°).
- [ ] Validate on calibrated goniometer bench at 0°, 30°, 60°, 90°, and 120° reference positions with mean absolute error $\le 2^\circ$.

## 📋 Subtasks
- [ ] Implement `calculate_angle_from_counts()` in `module1_hardware_encoder/src/main.c`.
- [ ] Record bench test calibration data and document final resolution constant in header.
