"""
CSV Data Logger Module — Synchronized Session Disk Exporter

Handles timestamped CSV session creation, buffered row writing,
and safe file closure for synchronized dual-modal kinematics records.

Project Team: Ibrahim Halil Dogan, Mert Canoglu, Cem Baygin, Cansu Bulut
"""

import csv
from datetime import datetime
from pathlib import Path
from typing import Optional, Dict, Any


class CSVLogger:
    """
    Session CSV recorder with buffered disk flushing and header management.

    Output schema:
        timestamp_ms, seq, left_count, right_count,
        left_angle, right_angle, camera_angle, visibility, valid_flag
    """

    FIELDNAMES = [
        "timestamp_ms",
        "seq",
        "left_count",
        "right_count",
        "left_angle",
        "right_angle",
        "camera_angle",
        "visibility",
        "valid_flag",
    ]

    def __init__(self, output_dir: str = "recordings") -> None:
        self.output_dir = Path(output_dir)
        self.output_dir.mkdir(parents=True, exist_ok=True)
        self._file = None
        self._writer: Optional[csv.DictWriter] = None
        self._row_count = 0

    def start_session(self, subject_id: str = "SUBJ_01", task_name: str = "SQUAT") -> Path:
        """
        Initializes a new recording file with standard session naming.

        TODO:
        - Format: session_YYYYMMDD_HHMMSS_<subject_id>_<task_name>.csv
        - Open file handle in write mode with newline=''
        - Initialize csv.DictWriter with self.FIELDNAMES
        - Write header row
        - Reset self._row_count = 0
        """
        timestamp_str = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"session_{timestamp_str}_{subject_id}_{task_name}.csv"
        file_path = self.output_dir / filename

        self._file = open(file_path, mode="w", newline="", encoding="utf-8")
        self._writer = csv.DictWriter(self._file, fieldnames=self.FIELDNAMES)
        self._writer.writeheader()
        self._row_count = 0
        return file_path

    def log_row(self, row_data: Dict[str, Any]) -> None:
        """
        Appends a synchronized data row to the active CSV session.

        TODO:
        - Validate that self._writer is active
        - Filter dictionary keys to match self.FIELDNAMES
        - Call writerow and increment self._row_count
        - Periodically flush buffer every 50 rows
        """
        if self._writer:
            filtered_data = {k: row_data.get(k, "") for k in self.FIELDNAMES}
            self._writer.writerow(filtered_data)
            self._row_count += 1
            if self._row_count % 50 == 0 and self._file:
                self._file.flush()

    def end_session(self) -> int:
        """
        Flushes and closes the active file handle.

        TODO:
        - Flush buffer and close self._file
        - Reset writer handle to None
        - Return total recorded row count
        """
        count = self._row_count
        if self._file:
            self._file.flush()
            self._file.close()
            self._file = None
            self._writer = None
        return count
