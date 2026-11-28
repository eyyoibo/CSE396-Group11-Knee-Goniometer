# Contributing Guidelines

This document outlines the development workflow, coding standards, branch conventions, and testing requirements for contributors to the **Dual-Encoder Wireless Knee Goniometer & Markerless Pose Estimation Comparison System**.

---

## 1. Development Workflow

1. Select an open issue from [GitHub Issues](https://github.com/eyyoibo/CSE396-Group11-Knee-Goniometer/issues) or create a new one.
2. Create a dedicated feature branch from `main` following our branch naming standards.
3. Write clean, self-documenting code and ensure all automated tests pass.
4. Submit a Pull Request (PR) referencing the issue.
5. Obtain review approval from at least one teammate before merging.

---

## 2. Branch Naming Standards

Branch names must clearly indicate the target module and scope of work:

```text
<type>/<module>/<short-description>
```

### Types
* `feature/`: New capability or component
* `fix/`: Bug resolution
* `refactor/`: Code reorganization without functional alteration
* `test/`: Adding or updating test suites
* `docs/`: Documentation additions or modifications

### Examples
```bash
feature/m1/pcnt-interrupt-handler
feature/m2/sliding-rmse-calculator
feature/m3/butterworth-filter
feature/m4/bluetooth-service-stubs
fix/m2/pyqtgraph-timestamp-axis
docs/architecture-synchronization-diagram
```

---

## 3. Commit Message Standards

Prefix every commit with the module tag:

| Tag | Scope |
|:---|:---|
| `[M1]` | Module 1: ESP32 Firmware & Hardware Signal Processing |
| `[M2]` | Module 2: Desktop GUI & RMSE Analysis |
| `[M3]` | Module 3: Computer Vision & MediaPipe Pose Estimation |
| `[M4]` | Module 4: Mobile Application |
| `[SHARED]` | Cross-module utilities, packet definitions, synthetic data |
| `[DOCS]` | Documentation, protocols, diagrams |
| `[CI]` | GitHub Actions, build configurations, linting rules |

### Example Commit Messages
```bash
git commit -m "[M1] Implement 4x quadrature PCNT hardware counter configuration"
git commit -m "[M2] Add circular buffer to sliding window RMSE calculator"
git commit -m "[M3] Implement vector dot product knee angle calculation"
git commit -m "[M4] Add AngleGauge SVG dial component"
git commit -m "[SHARED] Add CRC-16/CCITT verification in packet parser"
```

---

## 4. Pre-PR Verification & Testing

Before submitting a Pull Request, verify that all linters and tests pass locally:

### Python Subsystems (Module 2, Module 3, Shared, Tests)
```bash
# Run automated pytest suite
pytest tests/ -v

# Run flake8 syntax and style check
flake8 . --count --select=E9,F63,F7,F82 --show-source --statistics
```

### Firmware Subsystem (Module 1)
```bash
cd module1_hardware_encoder
pio run
```

### Mobile Subsystem (Module 4)
```bash
cd module4_mobile_app
npm run lint
```

---

## 5. Code Style Guidelines

* **Language Policy:** All identifiers (functions, variables, classes, constants), file names, and comments MUST be in **English**.
* **Python:** Strictly adhere to **PEP 8**. Use type hints on all function signatures. Use Google-style docstrings. Maximum line length: 100 characters.
* **C (ESP-IDF):** Follow Espressif C conventions. Use `snake_case` for functions and variables. Prefix module-level APIs (e.g., `pcnt_encoder_init()`).
* **TypeScript / React:** Follow Airbnb style guide. Prefer functional components with hooks.
* **No AI Attribution:** Never add AI assistants, chatbots, or automated generation tags as co-authors or contributors. All work is authored by project team members.
