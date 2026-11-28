#!/usr/bin/env python3
"""
update_remote_issues.py

Ensures all milestones exist on GitHub, then updates existing issues (#6 to #21)
with English titles, bodies, and milestones.
"""

import json
import os
import re
import subprocess
import tempfile
from pathlib import Path

REPO = "eyyoibo/CSE396-Group11-Knee-Goniometer"
ISSUES_DIR = Path(__file__).resolve().parent.parent / "docs" / "issues"

REQUIRED_MILESTONES = [
    "M1-Hardware Prototype",
    "M2-Desktop MVP",
    "M3-Camera Pipeline",
    "M4-Mobile App",
    "Integration"
]

MAPPING = {
    "issue_01_pcnt_driver.md": 6,
    "issue_02_differential_receiver.md": 7,
    "issue_03_bluetooth_spp.md": 8,
    "issue_04_angle_calculation_fw.md": 9,
    "issue_05_pyqt_gui_skeleton.md": 10,
    "issue_06_bt_serial_receiver.md": 11,
    "issue_07_live_plots.md": 12,
    "issue_08_rmse_analysis.md": 13,
    "issue_09_bland_altman.md": 14,
    "issue_10_csv_logger.md": 15,
    "issue_11_mediapipe_pipeline.md": 16,
    "issue_12_angle_from_camera.md": 17,
    "issue_13_time_sync.md": 18,
    "issue_14_simulation_overlay.md": 19,
    "issue_15_mobile_app.md": 20,
    "issue_16_synthetic_data.md": 21
}


def ensure_milestones():
    print(f"Checking existing milestones on {REPO}...")
    res = subprocess.run(["gh", "api", f"repos/{REPO}/milestones"], capture_output=True, text=True, check=True)
    existing = [m["title"] for m in json.loads(res.stdout)]
    print(f"Existing milestones: {existing}")

    for m in REQUIRED_MILESTONES:
        if m not in existing:
            print(f"Creating milestone: {m}")
            subprocess.run(["gh", "api", f"repos/{REPO}/milestones", "-f", f"title={m}"], capture_output=True, check=True)


def update_issues():
    print(f"\nUpdating issues on {REPO}...")
    for filename, issue_num in MAPPING.items():
        filepath = ISSUES_DIR / filename
        if not filepath.exists():
            continue

        content = filepath.read_text(encoding="utf-8")
        match = re.search(r"^---\s*\n(.*?)\n---\s*\n(.*)$", content, re.DOTALL)
        if not match:
            continue

        fm, body = match.group(1), match.group(2).strip()
        title_m = re.search(r'title:\s*["\']?(.*?)["\']?$', fm, re.MULTILINE)
        title = title_m.group(1) if title_m else filepath.stem

        milestone_m = re.search(r'milestone:\s*["\']?(.*?)["\']?$', fm, re.MULTILINE)
        milestone = milestone_m.group(1) if milestone_m else None

        with tempfile.NamedTemporaryFile("w", encoding="utf-8", delete=False, suffix=".md") as tf:
            tf.write(body)
            temp_name = tf.name

        try:
            cmd = ["gh", "issue", "edit", str(issue_num), "--repo", REPO, "--title", title, "--body-file", temp_name]
            if milestone:
                cmd.extend(["--milestone", milestone])
            subprocess.run(cmd, capture_output=True, text=True, check=True)
            print(f"[OK] #{issue_num}: {title} (Milestone: {milestone})")
        except subprocess.CalledProcessError as e:
            print(f"[ERROR] #{issue_num}: {e.stderr.strip()}")
        finally:
            if os.path.exists(temp_name):
                os.remove(temp_name)


def main():
    ensure_milestones()
    update_issues()
    print("\nAll issues updated successfully!")


if __name__ == "__main__":
    main()
