# CLAUDE.md - CSE 396 Group 11 Development Guide

This repository contains the **Wireless Wearable Dual-Encoder Knee Goniometer & Vision-Based Lower-Limb Kinematics Analyzer** for CSE 396 at Gebze Technical University, advised by Prof. Dr. Erkan Zergeroğlu.

---

## 👥 Team & Responsibilities
- **İbrahim Halil Doğan (`eyyoibo`)**: ESP32 Hardware/FreeRTOS, Dual-Encoder Kinematics, GitHub Actions CI/CD.
- **Mert Canoğlu**: Hardware interfacing & knee brace mechanical assembly, MediaPipe Pose tracking pipeline.
- **Cem Baygın**: Kinematic calibration algorithms, Real-time Desktop GUI & plotting engine.
- **Cansu Bulut**: Sagittal angle vector geometry, Real-time RMSE/MAE discrepancy analytics, Pytest test automation.

---

## ⚡ Daily Development Commands
```bash
# 1. Run unit tests
pytest tests/ -v

# 2. Run syntax and style linter (must pass for GitHub Actions CI green tick)
flake8 . --count --select=E9,F63,F7,F82 --show-source --statistics

# 3. Run desktop GUI simulation
python -m src.gui_app
```

---

## 🌿 Git Golden Workflow
1. **Never commit directly to `main`**.
2. Create a feature branch: `git checkout -b feature/<module-name>`
3. Write code and verify locally: `pytest tests/`
4. Commit and push:
   ```bash
   git add .
   git commit -m "feat(<module>): descriptive message"
   git push origin feature/<module-name>
   ```
5. Open a Pull Request (PR) on GitHub. Wait for GitHub Actions to turn green ($\checkmark$), request team review, and merge.

---

## 🤖 Claude Code Skills & Extensions
- **`superpowers`**: Autonomous test running, multi-file refactoring, and root-cause debugging.
- **`graphify`**: Visualizes module call graphs and dependency hierarchies across C++ and Python.
- **`caveman`**: Token-efficient, dense code generation mode for large algorithmic implementations.
- **`claude-mem`**: Persistent memory for hardware parameters (600 PPR, pin maps, mathematical baselines).
- **`ponytail`**: Natural language Git branch, commit, and PR management.
- **`rea`**: Static analysis of firmware ISR latencies and MediaPipe frame rendering pipelines.
- **`karpathy-skills`**: Clean, lightweight Python patterns with zero unnecessary abstractions.

---

## 🔌 Model Context Protocol (MCP) Servers
- **`figma`**: Converts GUI wireframes and dashboard mockups into PyQt/PySide layout code.
- **`playwright`**: Performs automated UI snapshot testing and visual verification of desktop dashboards.
- **`github`**: Direct management of GitHub Issues (#1 through #5), PR comments, and CI workflow status.
- **`sequential-thinking`**: Step-by-step mathematical reasoning for kinematic transformations and Kalman filtering.
