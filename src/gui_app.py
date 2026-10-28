"""GUI Control Panel & Real-Time 2D Plotter (Module 4).

Provides real-time visualization of lower-limb kinematics, synchronizing
dual-encoder telemetry from the ESP32 and optical pose estimation curves
from the camera feed, with instant RMSE / MAE discrepancy tracking.
"""

from typing import Dict, List, Optional
import time
from src.kinematics import calculate_rmse, calculate_mae


class GoniometerDashboard:
    """Manages synchronized telemetry streams, real-time metrics, and calibration."""

    def __init__(self, buffer_size: int = 500) -> None:
        self.buffer_size = buffer_size
        self.encoder_history: List[float] = []
        self.camera_history: List[float] = []
        self.timestamps: List[float] = []
        self.is_calibrated: bool = False
        self.zero_offset: float = 0.0

    def add_synchronized_sample(
        self,
        timestamp: float,
        angle_encoder: float,
        angle_camera: float,
    ) -> None:
        """Add a synchronized time-stamped measurement pair to the sliding window buffer."""
        calibrated_encoder = angle_encoder - self.zero_offset
        self.timestamps.append(timestamp)
        self.encoder_history.append(calibrated_encoder)
        self.camera_history.append(angle_camera)

        if len(self.timestamps) > self.buffer_size:
            self.timestamps.pop(0)
            self.encoder_history.pop(0)
            self.camera_history.pop(0)

    def calibrate_zero(self, reference_angle: float = 0.0) -> None:
        """One-click software calibration routine to re-zero encoder baseline offset."""
        if self.encoder_history:
            latest_raw = self.encoder_history[-1] + self.zero_offset
            self.zero_offset = latest_raw - reference_angle
        else:
            self.zero_offset = 0.0
        self.is_calibrated = True

    def get_realtime_metrics(self) -> Dict[str, Optional[float]]:
        """Compute instantaneous discrepancy metrics (RMSE and MAE) over current buffer."""
        if not self.encoder_history or not self.camera_history:
            return {"rmse": None, "mae": None, "samples": 0}

        rmse = calculate_rmse(self.encoder_history, self.camera_history)
        mae = calculate_mae(self.encoder_history, self.camera_history)
        return {
            "rmse": round(rmse, 2),
            "mae": round(mae, 2),
            "samples": len(self.encoder_history),
        }

    def export_csv(self, filepath: str) -> None:
        """Export synchronized kinematic trajectory data to CSV for offline analysis."""
        with open(filepath, "w", encoding="utf-8") as f:
            f.write("timestamp_sec,encoder_angle_deg,camera_angle_deg\n")
            for t, enc, cam in zip(self.timestamps, self.encoder_history, self.camera_history):
                f.write(f"{t:.4f},{enc:.2f},{cam:.2f}\n")


def run_demo() -> None:
    """Headless simulation demo for verification."""
    print("Initializing CSE396 Group 11 Knee Goniometer Dashboard...")
    dashboard = GoniometerDashboard()
    start = time.time()
    for i in range(50):
        t = time.time() - start
        # Simulated slight variance between encoder and vision
        enc_angle = 45.0 + (i * 0.5)
        cam_angle = 45.2 + (i * 0.5)
        dashboard.add_synchronized_sample(t, enc_angle, cam_angle)

    metrics = dashboard.get_realtime_metrics()
    print(f"Sample count: {metrics['samples']}")
    print(f"Instantaneous RMSE: {metrics['rmse']} deg | MAE: {metrics['mae']} deg")


if __name__ == "__main__":
    run_demo()
