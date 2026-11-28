---
title: "[M3] Vector Angle Calculation and Butterworth Low-Pass Filter"
labels: ["module-3", "software", "priority-high"]
milestone: "M3-Camera Pipeline"
assignees: ["Mert Canoglu", "Cansu Bulut"]
---

## 📌 Task Description
Compute the physiological knee flexion angle from tracked hip ($P_{\text{hip}}$), knee ($P_{\text{knee}}$), and ankle ($P_{\text{ankle}}$) landmarks using 2D vector dot products. Apply a 2nd-order low-pass Butterworth filter to suppress optical marker jitter.

## 🎯 Acceptance Criteria
- [ ] Construct segment vectors:
  $$\vec{u} = P_{\text{hip}} - P_{\text{knee}}$$
  $$\vec{v} = P_{\text{ankle}} - P_{\text{knee}}$$
- [ ] Interior angle formula:
  $$\alpha = \arccos\left(\frac{\vec{u} \cdot \vec{v}}{\|\vec{u}\| \|\vec{v}\|}\right)$$
- [ ] Knee flexion angle: $\theta_{\text{cam}} = 180^\circ - \alpha$ (full straight extension = $0^\circ$).
- [ ] Apply numerical clipping to cosine ratio (`np.clip(dot_val, -1.0, 1.0)`) to prevent domain errors.
- [ ] Apply 2nd-order low-pass Butterworth filter ($f_c \approx 6\text{ Hz}$, $f_s = 30\text{ Hz}$) to smooth high-frequency pose jitter.
- [ ] Validate angle calculation against known geometric calibration jigs (0°, 45°, 90°, 120°).

## 📋 Subtasks
- [ ] Implement `compute_angle()` and `apply_butterworth_filter()` in `module3_mediapipe_simulation/src/angle_calculator.py`.
- [ ] Validate implementation with unit tests in `tests/test_angle_calculator.py`.
