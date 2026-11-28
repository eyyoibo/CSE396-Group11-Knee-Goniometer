# Module 3: Simulation & MediaPipe Pose Angle Estimation

## Overview

This module implements the markerless optical motion capture pipeline. Utilizing a monocular RGB camera (1080p @ 30 FPS) positioned in the sagittal plane, it tracks lower-extremity body landmarks using Google MediaPipe Pose (BlazePose). Flexion-extension knee angles are computed through 2D vector kinematics, filtered with a low-pass Butterworth filter to suppress optical jitter, and time-aligned with the 50 Hz hardware encoder telemetry via linear timestamp interpolation.

Additionally, it renders a real-time 2D schematic kinematic skeleton overlay and live HUD on the video stream.

---

## Computer Vision Pipeline

1. **Frame Capture:** OpenCV `VideoCapture` acquires frames at 1920x1080 resolution and 30 FPS with microsecond monotonic timestamps.
2. **Preprocessing:** Frame color conversion from BGR to RGB format required by MediaPipe.
3. **Landmark Extraction:** Extracts 2D normalized coordinates for camera-facing lower-limb joints:
   - Hip: `LEFT_HIP (23)` or `RIGHT_HIP (24)`
   - Knee: `LEFT_KNEE (25)` or `RIGHT_KNEE (26)`
   - Ankle: `LEFT_ANKLE (27)` or `RIGHT_ANKLE (28)`
4. **Visibility & Occlusion Screening:** Evaluates landmark visibility scores. Frames exhibiting visibility below $0.6$ on any key joint are flagged as invalid and excluded from discrepancy calculations.

---

## Mathematical Formulations

### 1. Vector Dot Product Angle Calculation
From extracted sagittal joint coordinates:
$$\vec{u} = P_{hip} - P_{knee}$$
$$\vec{v} = P_{ankle} - P_{knee}$$

$$\cos(\alpha) = \text{clip}\left(\frac{\vec{u} \cdot \vec{v}}{\|\vec{u}\| \|\vec{v}\|}, -1.0, 1.0\right)$$
$$\alpha = \arccos(\cos(\alpha)) \cdot \frac{180^\circ}{\pi}$$
$$\theta_{camera} = 180^\circ - \alpha$$

*(Anatomical straight-leg standing position corresponds to approximately $0^\circ$ flexion).*

### 2. Jitter Attenuation (Butterworth Low-Pass Filter)
Human joint kinematics typically operate below 6 Hz. A 2nd-order digital Butterworth filter is applied:
- Cutoff frequency ($f_c$): $6.0\text{ Hz}$
- Sampling rate ($f_s$): $30\text{ Hz}$ (Camera frame rate)
- Implementation: Zero-phase forward-backward filtering (`scipy.signal.filtfilt`)

### 3. Temporal Synchronization & Interpolation
To compare 30 FPS optical angles with 50 Hz encoder telemetry:
- Hardware uptime timestamps and PC system timestamps are aligned at session start.
- `np.interp` linearly interpolates optical angles onto the continuous 50 Hz hardware timestamps.
- Missing or occluded frames are preserved as `NaN` values to avoid interpolation artifacts.

---

## 2D Kinematic Simulation Overlay

The rendering engine overlays the following graphics onto the real-time video feed:
* **Segment Links (Bones):** Color-coded lines connecting Hip $\rightarrow$ Knee $\rightarrow$ Ankle.
* **Joint Centers:** Circular highlights at detected landmark positions.
* **Angle Arc:** Dynamic arc centered at the knee joint indicating measured flexion.
* **HUD Information Panel:** Semi-transparent panel showing:
  - Instantaneous Knee Angle (degrees)
  - Landmark Visibility Score ($0.0 - 1.0$)
  - Live Processing FPS
  - Session Frame Counter

---

## Dependencies & Installation

```bash
pip install -r requirements.txt
```

| Package | Minimum Version | Description |
|---|---|---|
| `mediapipe` | $\ge 0.10.0$ | BlazePose landmark detection model |
| `opencv-python` | $\ge 4.8.0$ | Video capture and real-time graphics rendering |
| `numpy` | $\ge 1.24.0$ | Vector trigonometry and array interpolation |
| `scipy` | $\ge 1.11.0$ | Butterworth filter design and signal processing |

---

## TODO Checklist

- [ ] Implement OpenCV camera thread in `camera_capture.py`
- [ ] Implement MediaPipe Pose inference wrapper in `pose_detector.py`
- [ ] Implement vector angle calculation and zero-clamping in `angle_calculator.py`
- [ ] Implement Butterworth filter in `angle_calculator.py`
- [ ] Implement linear interpolation in `angle_calculator.py`
- [ ] Implement 2D schematic skeleton and HUD overlay in `simulation_renderer.py`
