---
title: "[M3] 2D Skeletal Simulation Overlay and Live Telemetry Heads-Up Display"
labels: ["module-3", "software", "priority-medium"]
milestone: "M3-Camera Pipeline"
assignees: ["Cem Baygin", "Mert Canoglu"]
---

## 📌 Task Description
Render a 2D skeletal line overlay (thigh and shank segments), dynamic joint angle arc, and semi-transparent telemetry Heads-Up Display (HUD) directly onto the live OpenCV video stream.

## 🎯 Acceptance Criteria
- [ ] Draw skeletal bones (`cv2.line`) and joint nodes (`cv2.circle`) connecting hip, knee, ankle, and foot landmarks.
- [ ] Draw dynamic angle arc (`cv2.ellipse`) centered at the knee joint representing flexion angle span.
- [ ] Semi-transparent HUD overlay in top corner displaying:
  - Instantaneous Knee Angle: `XX.X°`
  - Landmark Confidence Score: `0.XX`
  - Video Processing Throughput: `XX FPS`
- [ ] Explicitly note that this rendering is a 2D geometric visualization of measured kinematic angles, not an anatomical 3D simulation or clinical diagnostic model.

## 📋 Subtasks
- [ ] Implement `draw_skeleton_overlay()`, `draw_angle_arc()`, and `draw_info_panel()` in `module3_mediapipe_simulation/src/simulation_renderer.py`.
- [ ] Optimize overlay drawing pipeline to minimize video frame rendering latency.
