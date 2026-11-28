---
title: "[M3] OpenCV 1080p Video Stream and MediaPipe Pose Extraction"
labels: ["module-3", "software", "priority-high"]
milestone: "M3-Camera Pipeline"
assignees: ["Mert Canoglu", "Cansu Bulut"]
---

## 📌 Task Description
Acquire a 1080p @ 30 FPS sagittal video stream from a tripod-mounted camera using OpenCV. Run the pre-trained **MediaPipe Pose (BlazePose)** model locally to extract normalized 2D landmark coordinates and confidence scores for key lower-limb anatomical joints (hip, knee, ankle, foot index).

## 🎯 Acceptance Criteria
- [ ] Initialize camera stream via OpenCV `VideoCapture` confirming 1920x1080 resolution at 30 FPS.
- [ ] Convert BGR frames to RGB and feed into MediaPipe Pose (`model_complexity=1`).
- [ ] Extract keypoints for the camera-facing limb:
  - Left Leg: `LEFT_HIP (23)`, `LEFT_KNEE (25)`, `LEFT_ANKLE (27)`
  - Right Leg: `RIGHT_HIP (24)`, `RIGHT_KNEE (26)`, `RIGHT_ANKLE (28)`
- [ ] Extract `(x, y, visibility)` for each joint; flag frames with `visibility < 0.6` as invalid/occluded.
- [ ] Maintain an end-to-end processing throughput of at least 25 FPS on the host PC.

## 📋 Subtasks
- [ ] Implement `start()` and `read_frame()` in `module3_mediapipe_simulation/src/camera_capture.py`.
- [ ] Implement pose extraction logic in `module3_mediapipe_simulation/src/pose_detector.py`.
