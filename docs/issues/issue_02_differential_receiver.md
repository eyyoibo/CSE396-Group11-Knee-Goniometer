---
title: "[M1] Differential Line Receiver Circuit Design and Interfacing"
labels: ["module-1", "hardware", "priority-high"]
milestone: "M1-Hardware Prototype"
assignees: ["Cem Baygin", "Mert Canoglu"]
---

## 📌 Task Description
Long wiring harness runs from the rotary encoders carry differential quadrature signals ($A, \bar{A}, B, \bar{B}$) that are susceptible to ambient electromagnetic interference (EMI). Design and interface an intermediate signal conditioning circuit using the **AM26C32** (or equivalent) quad differential line receiver to reject common-mode noise and safely convert encoder pulses to ESP32-compatible 3.3V CMOS logic levels.

## 🎯 Acceptance Criteria
- [ ] Connect left and right encoder differential pairs to AM26C32 inputs with 120-ohm differential termination resistors.
- [ ] Verify using a multimeter and oscilloscope that receiver outputs strictly do not exceed 3.3V logic level.
- [ ] Establish a single-point star ground connecting ESP32 GND and encoder power ground to prevent ground loops.
- [ ] Document complete schematic, resistor values, and pin mapping table in `module1_hardware_encoder/docs/WIRING.md`.

## 📋 Subtasks
- [ ] Solder prototype circuit on perforated prototyping board.
- [ ] Verify 90° phase shift between A and B channels during rapid manual rotation using a logic analyzer.
- [ ] Layout packaging enclosure for secure waist-belt mounting during athletic movements.
