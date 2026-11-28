"""
Angle Calculator Module — Vector Trigonometry & Signal Filtering

Calculates knee flexion-extension angles from 2D joint coordinates
using vector dot products, applies digital Butterworth low-pass filtering,
and performs linear temporal interpolation onto hardware timestamps.

Project Team: Ibrahim Halil Dogan, Mert Canoglu, Cem Baygin, Cansu Bulut
"""

from typing import Tuple
import numpy as np


class AngleCalculator:
    """
    Vector trigonometry, signal filtering, and timestamp interpolation.
    """

    def compute_angle(
        self,
        hip_point: Tuple[float, float],
        knee_point: Tuple[float, float],
        ankle_point: Tuple[float, float],
    ) -> float:
        """
        Calculates 2D knee flexion angle using vector dot product:
            u = P_hip - P_knee
            v = P_ankle - P_knee
            cos(alpha) = clip( (u . v) / (|u| * |v|), -1.0, 1.0 )
            theta_cam = 180.0 - arccos(cos(alpha))

        Args:
            hip_point: (x, y) 2D pixel coordinates of the hip.
            knee_point: (x, y) 2D pixel coordinates of the knee.
            ankle_point: (x, y) 2D pixel coordinates of the ankle.

        Returns:
            Knee flexion angle in degrees (0.0 to 180.0 range).
        """
        u = np.array([hip_point[0] - knee_point[0], hip_point[1] - knee_point[1]], dtype=np.float64)
        v = np.array([ankle_point[0] - knee_point[0], ankle_point[1] - knee_point[1]], dtype=np.float64)

        norm_u = np.linalg.norm(u)
        norm_v = np.linalg.norm(v)

        if norm_u < 1e-6 or norm_v < 1e-6:
            return 0.0

        cos_alpha = np.dot(u, v) / (norm_u * norm_v)
        cos_alpha_clamped = np.clip(cos_alpha, -1.0, 1.0)
        alpha_deg = float(np.degrees(np.arccos(cos_alpha_clamped)))
        return float(180.0 - alpha_deg)

    def apply_butterworth_filter(
        self,
        signal: np.ndarray,
        cutoff_hz: float = 6.0,
        fs: float = 30.0,
        order: int = 2,
    ) -> np.ndarray:
        """
        Applies a zero-phase 2nd-order low-pass Butterworth filter.

        Args:
            signal: 1D NumPy array of raw angle values.
            cutoff_hz: Cutoff frequency in Hz (default: 6.0 Hz).
            fs: Camera frame rate (default: 30.0 FPS).
            order: Filter order (default: 2).

        Returns:
            Filtered 1D NumPy angle array.
        """
        from scipy.signal import butter, filtfilt

        if len(signal) <= 3 * order:
            return signal

        nyquist = 0.5 * fs
        normal_cutoff = cutoff_hz / nyquist
        b, a = butter(order, normal_cutoff, btype="low", analog=False)
        return filtfilt(b, a, signal)

    def interpolate_to_encoder_timestamps(
        self,
        camera_timestamps: np.ndarray,
        camera_angles: np.ndarray,
        encoder_timestamps: np.ndarray,
    ) -> np.ndarray:
        """
        Linearly interpolates optical angles onto continuous hardware encoder timestamps.

        Args:
            camera_timestamps: 1D array of optical frame timestamps (seconds).
            camera_angles: 1D array of optical joint angles (degrees).
            encoder_timestamps: 1D array of hardware encoder timestamps (seconds).

        Returns:
            Time-aligned angle array matching encoder timestamps.
        """
        if len(camera_timestamps) == 0 or len(camera_angles) == 0:
            return np.full_like(encoder_timestamps, np.nan, dtype=np.float64)

        # Linear interpolation with NaN filling for extrapolation bounds
        aligned_angles = np.interp(
            encoder_timestamps,
            camera_timestamps,
            camera_angles,
            left=np.nan,
            right=np.nan,
        )
        return aligned_angles
