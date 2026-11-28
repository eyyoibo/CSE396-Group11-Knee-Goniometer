# Experimental Validation & Motion Capture Protocol

**Project Team (Group 11):** İbrahim Halil Doğan, Mert Canoğlu, Cem Baygın, Cansu Bulut  
**Department of Computer Engineering**

---

## 1. Ethical Principles & Participant Privacy

1. **Informed Consent:** All volunteer participants are provided with a written explanation detailing the objective, procedure, sensor placement, and non-invasive camera recording prior to participation. Written informed consent is obtained from every participant.
2. **Data Anonymization:**
   - Each participant is assigned an anonymized unique identifier (e.g., `SUBJ_01`, `SUBJ_02`).
   - The RGB camera is positioned strictly to frame the lower extremities (waist-down), preventing facial feature capture.
   - Raw video files and sensor telemetry are processed locally on offline machines and will not be transferred to third-party cloud services.
3. **Voluntary Participation:** Participants retain the right to halt the session or withdraw at any moment without providing justification.

---

## 2. Participant Criteria & Sample Size

- **Target Cohort:** Minimum 15 completed, quality-screened participant datasets (up to 18 volunteers recruited to account for potential technical data exclusion).
- **Inclusion Criteria:**
  - Healthy adults aged 18 and older.
  - Ability to independently execute routine physical movements (squatting, chair rise, walking) without assistance or discomfort.
- **Exclusion Criteria:**
  - History of lower-limb surgical intervention within the preceding 6 months or active orthopedic joint pathologies.
  - Self-reported acute musculoskeletal pain, dizziness, or mobility impairment during initial warm-up.

---

## 3. Hardware & Camera Setup Geometry

```text
               [Stationary Monocular RGB Camera (1080p @ 30 FPS)]
                                      |
                                      | 2.5 - 3.0 meters orthogonal distance
                                      v
   +-----------------------------------------------------------------------+
   |                     Sagittal Plane Motion Corridor                     |
   |                                                                       |
   |  Participant (Waist ESP32 enclosure + Left/Right Polycentric Braces) |
   |                                                                       |
   +-----------------------------------------------------------------------+
```

- **Camera Positioning:** Fixed on a leveled tripod at knee height (~50 cm above ground), aligned orthogonal (90°) to the sagittal plane of motion.
- **Distance:** Maintained consistently between 2.5 and 3.0 meters from the subject's track.
- **Lighting & Contrast:** Diffuse, uniform indoor illumination to minimize ground shadows and optical glare.
- **Apparel:** Dark, fitted shorts that expose the patellar region and lateral joint line to facilitate clear landmark recognition without marker obstruction.

---

## 4. Functional Movement Protocols

Each participant completes two recording sessions: Session A with the left leg facing the camera, and Session B with the right leg facing the camera. Both knee braces continuously log dual-encoder telemetry throughout both sessions.

### Task 1: Controlled Squat
- **Repetitions:** 3 full repetitions at a self-selected, comfortable cadence.
- **Initial Stance:** Upright stance with feet shoulder-width apart (calibrated $0^\circ$ baseline).
- **Movement:** Controlled descent until knee flexion reaches approximately $90^\circ$, followed by return to upright extension.
- **Rest Interval:** 5 seconds between repetitions; 1 minute rest before the next task.

### Task 2: Sit-to-Stand (Chair Rise)
- **Repetitions:** 3 repetitions from a standard armless chair.
- **Initial Stance:** Seated upright with back straight and feet firmly planted.
- **Movement:** Stand fully upright without arm support, maintain extension for 2 seconds, and return smoothly to seated position.

### Task 3: Linear Walking Gait
- **Passes:** 5 continuous walking passes across a 5-meter obstacle-free track.
- **Capture Window:** Approximately 1-2 complete gait cycles (stance and swing phases) recorded per camera pass.

---

## 5. Calibration & Data Acquisition Sequence

1. **Pre-Flight Check:** Verify ESP32 battery level (>3.7V), confirm Bluetooth Classic SPP connection to the desktop station, and check 50 Hz packet reception.
2. **Zero-Extension Reference (`'Z'` Command):** While the participant stands motionless in anatomical zero extension, transmit `'Z'`. The ESP32 captures current encoder pulse counts as $N_{offset}$ ($0.0^\circ$), and the desktop software records the baseline optical angle.
3. **Session Initiation (`'S'` Command):** Transmit `'S'` to begin logging 50 Hz telemetry and 30 FPS video frames with synchronized timestamps.
4. **Session Termination (`'P'` Command):** Transmit `'P'` upon task completion. The CSV logger flushes buffers to disk (`session_<TIMESTAMP>_<SUBJ>_<TASK>.csv`).
5. **Quality Screening:** Verify that mean MediaPipe landmark visibility remains $v \ge 0.6$ and packet drop is $<1\%$. Flag trials exhibiting brace displacement for exclusion analysis.
