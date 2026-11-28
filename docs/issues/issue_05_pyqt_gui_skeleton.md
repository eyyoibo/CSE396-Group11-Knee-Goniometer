---
title: "[M2] PyQt6 Desktop Dashboard Architecture and Layout Skeleton"
labels: ["module-2", "software", "priority-high"]
milestone: "M2-Desktop MVP"
assignees: ["Cem Baygin", "Cansu Bulut"]
---

## 📌 Task Description
Construct the Python PyQt6 desktop user interface architecture and layout. The dashboard organizes connection and session controls on the left, real-time synchronized time-series plots in the center, and live error metrics (RMSE/MAE) and camera feed display on the right.

## 🎯 Acceptance Criteria
- [ ] Implement responsive dark-theme stylesheet on top of `QMainWindow`.
- [ ] Top Toolbar: Serial port dropdown (COM port / RFCOMM device), "Connect/Disconnect", "Zero [Z]", "Start [S]", "Pause [P]", and "Export CSV" actions.
- [ ] Global keyboard shortcuts mapped to 'Z', 'S', and 'P'.
- [ ] Status Bar: Connection status indicator, instantaneous packet throughput (Hz), elapsed session timer, and disk logging indicator.

## 📋 Subtasks
- [ ] Implement `init_ui()` layout and widget composition in `module2_interface_rmse/src/main_window.py`.
- [ ] Connect Qt signals and slots for control buttons and status updates.
