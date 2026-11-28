"""
Statistical Discrepancy Engine — RMSE, MAE & Bland-Altman Analytics

Computes sliding-window and cumulative statistical discrepancy metrics
between rotary encoder angular telemetry and optical pose estimation series.

Project Team: Ibrahim Halil Dogan, Mert Canoglu, Cem Baygin, Cansu Bulut
"""

from typing import Tuple, Dict, Any
import numpy as np


class AnalysisEngine:
    """
    Statistical engine for evaluating cross-modal kinematics tracking agreement.

    Default sliding window: 5.0 seconds (250 samples @ 50 Hz).
    """

    def __init__(self, window_seconds: float = 5.0, sample_rate_hz: float = 50.0) -> None:
        self.window_size = int(window_seconds * sample_rate_hz)
        self.encoder_buffer = []
        self.camera_buffer = []

    def compute_sliding_rmse(self, encoder_values: np.ndarray,
                             camera_values: np.ndarray) -> float:
        """
        Calculates Root Mean Square Error (RMSE) across the trailing window:
            RMSE = sqrt( (1/n) * sum((theta_cam_i - theta_enc_i)^2) )

        TODO:
        - Extract trailing window_size valid samples from arrays
        - Compute element-wise squared differences
        - Return square root of mean squared error
        """
        if len(encoder_values) == 0 or len(camera_values) == 0:
            return 0.0
        diff = camera_values[-self.window_size:] - encoder_values[-self.window_size:]
        return float(np.sqrt(np.mean(diff ** 2)))

    def compute_sliding_mae(self, encoder_values: np.ndarray,
                            camera_values: np.ndarray) -> float:
        """
        Calculates Mean Absolute Error (MAE) across the trailing window:
            MAE = (1/n) * sum(|theta_cam_i - theta_enc_i|)

        TODO:
        - Extract trailing window_size valid samples from arrays
        - Compute element-wise absolute differences
        - Return mean of absolute error
        """
        if len(encoder_values) == 0 or len(camera_values) == 0:
            return 0.0
        diff = np.abs(camera_values[-self.window_size:] - encoder_values[-self.window_size:])
        return float(np.mean(diff))

    def compute_bland_altman(self, encoder_series: np.ndarray,
                             camera_series: np.ndarray) -> Dict[str, float]:
        """
        Computes Bland-Altman method comparison parameters:
        - Mean difference (systematic bias, d_bar)
        - Standard deviation of differences (SD)
        - Upper 95% limit of agreement (d_bar + 1.96 * SD)
        - Lower 95% limit of agreement (d_bar - 1.96 * SD)

        TODO:
        - Filter out any NaN entries from camera occlusions
        - Compute pairwise differences D = camera_series - encoder_series
        - Compute mean bias and standard deviation
        - Return dictionary containing: bias, sd, upper_loa, lower_loa
        """
        valid_mask = ~np.isnan(camera_series) & ~np.isnan(encoder_series)
        enc_valid = encoder_series[valid_mask]
        cam_valid = camera_series[valid_mask]

        if len(enc_valid) == 0:
            return {"bias": 0.0, "sd": 0.0, "upper_loa": 0.0, "lower_loa": 0.0}

        differences = cam_valid - enc_valid
        bias = float(np.mean(differences))
        sd = float(np.std(differences, ddof=1)) if len(differences) > 1 else 0.0

        return {
            "bias": bias,
            "sd": sd,
            "upper_loa": bias + 1.96 * sd,
            "lower_loa": bias - 1.96 * sd
        }
