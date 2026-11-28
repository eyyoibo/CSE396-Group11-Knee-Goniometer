# GitHub Projects Setup & Sprint Management Guide

This document outlines how to organize, track, and execute development using GitHub Projects for the **Dual-Encoder Wireless Knee Goniometer & Markerless Pose Estimation Comparison System**.

---

## 1. Kanban Board Architecture

Create a project board titled **"Knee Goniometer & Pose Estimation — Engineering Board"** under your repository.

### Columns Definition

| Column | Purpose | Workflow Trigger |
|:---|:---|:---|
| **Backlog** | All defined features, issue backlog, and future ideas | New issues are triaged here |
| **To Do (Ready)** | Tasks planned and committed for the active 2-week sprint | Moved during sprint planning |
| **In Progress** | Tasks actively being developed by an assignee | Moved when a branch is created |
| **Review / Testing** | Code review, bench testing, and CI verification | Moved when a PR is opened |
| **Done** | Merged PRs, verified hardware/bench tests | Moved when PR merges to `main` |

---

## 2. Standard Issue Labels

| Category | Label | Color | Description |
|:---|:---|:---|:---|
| **Module** | `module-1` | `#1d76db` | Module 1: Hardware & Encoder Signal Processing |
| | `module-2` | `#0e8a16` | Module 2: Desktop Interface & RMSE Analysis |
| | `module-3` | `#d93f0b` | Module 3: Simulation & MediaPipe Pose Estimation |
| | `module-4` | `#5319e7` | Module 4: Mobile Application |
| **Type** | `hardware` | `#f9d0c4` | Physical wiring, PCB, sensors, breadboards |
| | `software` | `#c5def5` | Firmware, desktop GUI, vision math, mobile app |
| | `testing` | `#bfd4f2` | Unit tests, synthetic validation, bench testing |
| | `bug` | `#d73a4a` | Defect or unexpected behavior |
| | `enhancement` | `#a2eeef` | New feature or optimization |
| | `documentation`| `#0075ca` | Architecture, README, protocol updates |
| **Priority**| `priority-high` | `#b60205` | Critical path — blocking other components |
| | `priority-medium`| `#fbca04` | Standard sprint backlog item |
| | `priority-low` | `#0e8a16` | Non-blocking enhancement or cleanup |

---

## 3. Milestones & Delivery Roadmap

### Milestone 1: M1-Hardware Prototype
* **Focus:** ESP32 PCNT hardware pulse counter, differential line receiver, and 50 Hz Bluetooth SPP streaming.
* **Verification:** 5-minute continuous bench stream with $<1\%$ packet loss and $\le 2^\circ$ bench calibration error.

### Milestone 2: M2-Desktop MVP
* **Focus:** PyQt6 desktop GUI, real-time PyQtGraph plotting ($N(t)$, $\Delta N(t)$, $\theta(t)$), rolling 5s RMSE/MAE calculations, and CSV logging.
* **Verification:** Validated using synthetic packet stream generator at 50 Hz.

### Milestone 3: M3-Camera Pipeline
* **Focus:** 1080p @ 30 FPS OpenCV capture, MediaPipe Pose lower-limb landmark extraction, 2D vector trigonometry, and Butterworth filtering.
* **Verification:** Angular accuracy verified against known reference angle calibration templates.

### Milestone 4: M4-Mobile App
* **Focus:** Cross-platform React Native / Expo application, Bluetooth stream reader, live angular dial gauge, and remote Z/S/P controls.
* **Verification:** Standalone wireless testing on a physical mobile device.

### Milestone 5: Integration & Bench Validation
* **Focus:** Hardware timestamp alignment via linear interpolation, dual-modal cross-correlation latency assessment ($\le 33\text{ ms}$), Bland-Altman statistical analysis, and final report delivery.

---

## 4. Sprint Cadence (2-Week Iterations)

* **Team Members:** İbrahim Halil Doğan, Mert Canoğlu, Cem Baygın, Cansu Bulut
* **Sprint Planning:** Alternate Mondays (30 minutes). Select issues from Backlog into To Do.
* **Review & Retrospective:** Alternate Fridays (30 minutes). Demo progress and verify closed issues.
* **Target Velocity:** ~20-25 story points per sprint across the 4 engineers.
