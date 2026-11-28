---
title: "[M2] Bland-Altman Method Comparison and 95% Limits of Agreement"
labels: ["module-2", "software", "priority-medium"]
milestone: "M2-Desktop MVP"
assignees: ["Cem Baygin", "Cansu Bulut"]
---

## 📌 Task Description
Develop the Bland-Altman statistical analysis pipeline to evaluate clinical and technical agreement between markerless camera-based pose estimation and wearable electromechanical encoder measurements.

## 🎯 Acceptance Criteria
- [ ] Sample pairwise mean: $S_i = \frac{\theta_{\text{cam}}(t_i) + \theta_{\text{enc}}(t_i)}{2}$
- [ ] Sample pairwise difference: $D_i = \theta_{\text{cam}}(t_i) - \theta_{\text{enc}}(t_i)$
- [ ] Mean Difference (Bias): $\bar{D} = \frac{1}{N}\sum D_i$
- [ ] Standard deviation of differences ($SD$).
- [ ] 95% Limits of Agreement (LoA):
  $$\text{Upper Limit} = \bar{D} + 1.96 \cdot SD$$
  $$\text{Lower Limit} = \bar{D} - 1.96 \cdot SD$$
- [ ] Generate high-resolution scatter plot using Matplotlib with annotated bias and LoA dashed lines, exportable to PNG.
- [ ] Support repeated measures adjustment following Bland & Altman (2007) guidelines for non-independent trials across subjects.

## 📋 Subtasks
- [ ] Implement `compute_bland_altman()` in `module2_interface_rmse/src/analysis_engine.py`.
- [ ] Validate implementation with synthetic test cases in `tests/test_analysis_engine.py`.
