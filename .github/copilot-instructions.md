# Copilot Instructions — Knee Goniometer & Pose Estimation

## Project Context
This is an engineering kinematics project that builds a wearable wireless knee goniometer using two incremental rotary encoders interfaced with an ESP32 microcontroller, and cross-validates its measurements against single-camera markerless pose estimation (MediaPipe Pose).

## Team Members
- İbrahim Halil Doğan
- Mert Canoğlu
- Cem Baygın
- Cansu Bulut

## Code Style Preferences
- **Language Policy:** All code, comments, docstrings, and documentation MUST be in English.
- **Python (M2, M3, shared):** Strict PEP 8, full type hints, Google-style docstrings, line length $\le 100$ characters.
- **C (M1):** ESP-IDF conventions, `snake_case`, packed binary structs matching the 28-byte packet specification.
- **TypeScript (M4):** Airbnb style guide, functional components with hooks, strict typing.

## Architectural Boundaries
- Keep module boundaries strictly separated.
- Shared logic lives exclusively in `shared/`.
- The 28-byte binary packet format (`0xAA 0x55` header, 50 Hz streaming) is the canonical hardware-software contract.
- Never add AI, automated bots, or assistant names as contributors or co-authors.
