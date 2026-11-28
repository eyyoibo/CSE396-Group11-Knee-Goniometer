---
title: "[M3] Hardware Timestamp Synchronization and Interpolation Engine"
labels: ["module-3", "module-2", "software", "priority-high"]
milestone: "Integration"
assignees: ["Ibrahim Halil Dogan", "Cansu Bulut"]
---

## 📌 Task Description
The external optical camera operates at 30 FPS (~33.3 ms sampling interval) while the ESP32 encoder telemetry streams at 50 Hz (20 ms interval). Align both asynchronous streams onto a common monotonic timeline using linear temporal interpolation for valid cross-modal error analysis.

## 🎯 Acceptance Criteria
- [ ] Determine baseline epoch offset $\Delta t_{\text{offset}}$ between ESP32 hardware millisecond counter ($t_{\text{ESP}}$) and host PC clock ($t_{\text{PC}}$).
- [ ] Linearly interpolate camera angle samples onto encoder packet timestamps using `np.interp`.
- [ ] Occluded frames with low visibility confidence must be omitted from interpolation and masked as `NaN`.
- [ ] Validate cross-correlation lag on controlled cyclic squats, ensuring residual phase delay is within 1 camera frame ($\le 33\text{ ms}$).

## 📋 Subtasks
- [ ] Implement `interpolate_to_encoder_timestamps()` in `module3_mediapipe_simulation/src/angle_calculator.py`.
- [ ] Construct integration test verifying timestamp alignment accuracy.
