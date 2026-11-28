---
title: "[M2] Real-Time Multi-Curve Visualization with PyQtGraph"
labels: ["module-2", "software", "priority-medium"]
milestone: "M2-Desktop MVP"
assignees: ["Mert Canoglu", "Cansu Bulut"]
---

## 📌 Task Description
Implement high-performance hardware-accelerated time-series plots using the PyQtGraph library to display three dynamic data streams:
1. **Angle vs. Time ($\theta(t)$):** Left knee encoder angle (blue), right knee encoder angle (green), and MediaPipe vision angle for the active limb (dashed red).
2. **Cumulative Count ($N(t)$):** Raw cumulative pulse counts from both encoders.
3. **Inter-Sample Count Delta ($\Delta N(t) = N(t) - N(t-1)$):** Instantaneous angular velocity indicator.

## 🎯 Acceptance Criteria
- [ ] Embed PyQtGraph `PlotWidget` instances maintaining a smooth 30-50 FPS UI refresh rate.
- [ ] Implement a trailing 10-second sliding time window on the X-axis; scale Y-axis from 0° to 150°.
- [ ] Decouple rendering from data acquisition using a dedicated `QTimer` at ~30 Hz.
- [ ] Include clear axis labels, physical units, dynamic legends, and grid lines.

## 📋 Subtasks
- [ ] Embed 3 plot panels into the central area of `main_window.py`.
- [ ] Implement circular buffers (`collections.deque`) in `update_plots()` for efficient O(1) appending and slicing.
