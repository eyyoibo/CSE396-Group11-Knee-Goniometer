---
title: "[M2] Synchronized Multi-Column CSV Data Logging Subsystem"
labels: ["module-2", "software", "priority-medium"]
milestone: "M2-Desktop MVP"
assignees: ["Cansu Bulut", "Ibrahim Halil Dogan"]
---

## 📌 Task Description
Implement a robust multi-channel CSV logger that records synchronized timestamps, raw encoder counts, computed angles, MediaPipe landmark coordinates, and confidence scores for every session bounded by 'S' (Start) and 'P' (Pause) commands.

## 🎯 Acceptance Criteria
- [ ] File naming standard: `session_YYYYMMDD_HHMMSS_<SubjectID>_<Task>.csv`.
- [ ] Required CSV header columns:
  `timestamp_ms, seq_num, enc_left_count, enc_right_count, enc_left_deg, enc_right_deg, cam_deg, cam_visibility, valid_flag`
- [ ] Buffered non-blocking disk I/O with periodic flush intervals to avoid GUI thread latency.
- [ ] Automatically flush remaining buffer and close file cleanly on 'P' command or application shutdown.

## 📋 Subtasks
- [ ] Implement `CsvLogger` class in `module2_interface_rmse/src/csv_logger.py`.
- [ ] Validate output format against reference specification in `shared/sample_session.csv`.
