# Copilot Instructions for Knee Goniometer & Pose Estimation Project

## Project Context

This is a biomedical engineering graduation project that builds a **knee goniometer** using rotary encoders interfaced with an ESP32 microcontroller, and compares its angle measurements against **camera-based pose estimation** (MediaPipe). The system transmits encoder data over Bluetooth to a desktop GUI and a mobile app, while simultaneously capturing knee joint angles via computer vision. The two measurement streams are time-synchronized for accuracy comparison.

## Repository Structure

The project is organized into four modules:

- **M1 (Hardware & Firmware):** ESP-IDF based firmware running on ESP32. Reads quadrature encoder data, computes joint angles, and transmits 28-byte binary packets over Bluetooth Classic SPP and BLE.
- **M2 (Desktop GUI):** Python desktop application using PyQt6. Receives Bluetooth data, displays real-time angle graphs, logs measurement sessions to CSV.
- **M3 (Camera Pipeline):** Python module using OpenCV and MediaPipe. Captures video frames, detects body landmarks, calculates knee flexion/extension angles.
- **M4 (Mobile App):** React Native application. Connects to ESP32 via BLE, displays angle data, provides portable measurement capability.

## Code Style Preferences

### Python (M2, M3, shared utilities)
- Follow PEP 8 strictly
- Use type hints for all function signatures
- Docstrings in Google style format
- Maximum line length: 100 characters
- Use `pathlib.Path` over `os.path`

### C (M1 firmware)
- Follow ESP-IDF coding conventions
- Use `snake_case` for functions and variables
- Prefix module-specific functions with the module name (e.g., `encoder_read_angle()`)
- Comment hardware register interactions thoroughly

### JavaScript / TypeScript (M4)
- Follow Airbnb style guide
- Prefer functional components with hooks
- Use TypeScript where possible

## Module Boundaries

Each module has its own directory and should be self-contained:
- Do NOT import code from one module into another directly
- Shared functionality belongs in the `shared/` directory
- The 28-byte packet parser is shared between M1, M2, and M4 — keep implementations in sync
- Camera code stays in M3; Bluetooth code stays in M2/M4; firmware stays in M1

## Testing Expectations

- M2 and M3: Write pytest unit tests for all utility functions and data processing logic
- M1: Test with synthetic serial data before flashing to hardware
- M4: Use Jest for component and logic tests
- Integration tests should use the synthetic data generator from `shared/`

## Language Policy

- All code identifiers (variable names, function names, class names): **English**
- Documentation, comments, and user-facing strings: **Turkish is acceptable**
- README and architecture docs: **Turkish**
- Git commit messages: **Turkish with module prefix**

## Critical Rules

- Never list any AI tool or automated assistant as an author or contributor anywhere in the codebase
- Do not modify hardware pin configurations without explicit instruction
- Do not change the 28-byte packet format without updating all consuming modules
- Preserve all existing comments unless they are factually wrong
