# Agent Instructions — Knee Goniometer & Pose Estimation

## Repository Architecture & Guidelines for Autonomous AI Agents

This document defines architectural boundaries, coding standards, and operational invariants for AI coding assistants working in this repository.

---

## 1. Repository Structure Overview

```text
knee-goniometer-pose-estimation/
├── module1_hardware_encoder/      # ESP-IDF C firmware for ESP32 & PCNT hardware counter
├── module2_interface_rmse/        # PyQt6 desktop GUI & real-time RMSE/MAE analytics engine
├── module3_mediapipe_simulation/  # OpenCV + MediaPipe Pose pipeline & 2D kinematic simulation
├── module4_mobile_app/            # React Native (Expo) companion mobile application
├── shared/                        # Shared binary packet parser & synthetic stream generator
├── tests/                         # Pytest automated test suite
├── docs/                          # Technical protocols, screen flows, and issue catalog
└── scripts/                       # Automation CLI scripts
```

---

## 2. Team Information & Attribution Policy

* **Project Team Members:**
  - İbrahim Halil Doğan
  - Mert Canoğlu
  - Cem Baygın
  - Cansu Bulut
* **CRITICAL INVARIANT:** Never add yourself, automated agents, or AI tool names as an author, co-author, contributor, or copyright holder anywhere in commits, docstrings, or repository files. All contributions are credited strictly to the human project team.

---

## 3. Module Boundaries & Invariants

Each module is strictly encapsulated:
* **Module 1 (Firmware):** Does not import or depend on Python code. Must output fixed 28-byte binary packets matching `telemetry_packet.h`.
* **Module 2 (Desktop):** Consumes telemetry packets via `shared/packet_parser.py`. Must run non-blocking serial reading in a dedicated `QThread`.
* **Module 3 (Vision):** Encapsulates all OpenCV and MediaPipe dependencies. Must produce filtered angles and landmark visibility scores. Does not directly handle Bluetooth connections.
* **Module 4 (Mobile):** Encapsulates mobile TypeScript / React Native code. Communicates with ESP32 via Bluetooth SPP / BLE.
* **Shared:** Contains cross-module utilities (e.g., `packet_parser.py`, `synthetic_data_generator.py`). Any change to the 28-byte packet structure must be reflected in `shared/` and all consuming modules.

---

## 4. Code Standards & Language Policy

* **Language:** All code identifiers, docstrings, comments, commit messages, and documentation must be written in **English**.
* **Python:** Follow PEP 8 strictly. Type hints are mandatory on all public function and method signatures.
* **C:** Follow Espressif ESP-IDF guidelines. Snake_case naming, clean header guards, and packed structs.
* **Scaffolding Policy:** When creating drafts or skeletons, provide complete typed signatures, comprehensive docstrings, mathematical formulas, and actionable TODO comments without committing fake or broken production code.
