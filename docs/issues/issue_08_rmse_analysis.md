---
title: "[M2] Sliding-Window (5s) RMSE, MAE, and Peak Discrepancy Engine"
labels: ["module-2", "software", "priority-high"]
milestone: "M2-Desktop MVP"
assignees: ["Cem Baygin", "Cansu Bulut"]
---

## 📌 Task Description
Compute statistical discrepancy metrics between the encoder angle series and the temporally synchronized optical camera angle series. Provide real-time updates over a trailing 5-second sliding window during active motion, as well as cumulative summary statistics at session completion.

## 🎯 Formulas and Acceptance Criteria
- [ ] **Mean Absolute Error (MAE):**
  $$\text{MAE} = \frac{1}{N} \sum_{i=1}^{N} |\theta_{\text{cam}}(t_i) - \theta_{\text{enc}}(t_i)|$$
- [ ] **Root Mean Square Error (RMSE):**
  $$\text{RMSE} = \sqrt{\frac{1}{N} \sum_{i=1}^{N} (\theta_{\text{cam}}(t_i) - \theta_{\text{enc}}(t_i))^2}$$
- [ ] **Mean Bias ($\bar{d}$):**
  $$\bar{d} = \frac{1}{N} \sum_{i=1}^{N} (\theta_{\text{cam}}(t_i) - \theta_{\text{enc}}(t_i))$$
- [ ] **Peak Angle Discrepancy ($\Delta\theta_{\text{peak}}$):** Absolute angle difference recorded at the point of maximum flexion.
- [ ] Frames flagged as occluded or low-confidence (visibility < 0.6) must be excluded from error accumulation and tracked as an invalid frame percentage.
- [ ] Render live values in the dashboard metrics panel with visual tolerance thresholds (green: MAE < 3°, amber: 3°-6°, red: > 6°).

## 📋 Subtasks
- [ ] Implement `compute_sliding_rmse()` and `compute_sliding_mae()` in `module2_interface_rmse/src/analysis_engine.py`.
- [ ] Verify correctness using unit tests in `tests/test_analysis_engine.py`.
