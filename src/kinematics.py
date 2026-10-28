"""Kinematics & Calibration Module (Module 2).

Implements dual-encoder pulse-to-angle conversion, polycentric knee flexion
kinematic superposition, calibration routines, error metrics (RMSE/MAE),
and synthetic telemetry generation.
"""

from typing import Iterable, List, Tuple
import math


def calculate_encoder_angle(pulses: float, ppr: float = 600.0) -> float:
    """Convert raw encoder pulse count to degrees for a single encoder.

    Args:
        pulses: Net pulse count accumulated.
        ppr: Pulses Per Revolution of the rotary encoder (default: 600).

    Returns:
        Calibrated angle in degrees.
    """
    if ppr == 0:
        raise ValueError("Encoder PPR cannot be zero.")
    return (float(pulses) / float(ppr)) * 360.0


def calculate_dual_encoder_angle(
    delta_n1: float,
    delta_n2: float,
    k1: float = 360.0 / 600.0,
    k2: float = 360.0 / 600.0,
    theta_0: float = 0.0,
) -> float:
    """Calculate polycentric knee flexion angle from dual encoder pulse counts.

    Mathematical formulation from Project Proposal Section 2.2.1:
        theta_knee,enc(t) = theta_0 + k1 * delta_N1(t) + k2 * delta_N2(t)

    Args:
        delta_n1: Net pulse count of rotary encoder 1.
        delta_n2: Net pulse count of rotary encoder 2.
        k1: Angular calibration constant for encoder 1 (deg/pulse).
        k2: Angular calibration constant for encoder 2 (deg/pulse).
        theta_0: Baseline zero-extension offset (degrees).

    Returns:
        Estimated knee flexion angle in degrees.
    """
    return theta_0 + (k1 * float(delta_n1)) + (k2 * float(delta_n2))


def calculate_rmse(
    angles_enc: Iterable[float],
    angles_cam: Iterable[float],
) -> float:
    """Calculate Root Mean Square Error (RMSE) between encoder and camera measurements.

    Args:
        angles_enc: Sequence of angles measured by the wearable encoder.
        angles_cam: Sequence of angles measured by the optical camera system.

    Returns:
        RMSE value in degrees.
    """
    enc = list(angles_enc)
    cam = list(angles_cam)
    if len(enc) != len(cam):
        raise ValueError("Data sequences must have identical lengths.")
    if not enc:
        return 0.0

    squared_errors = [(e - c) ** 2 for e, c in zip(enc, cam)]
    mean_squared_error = sum(squared_errors) / len(squared_errors)
    return math.sqrt(mean_squared_error)


def calculate_mae(
    angles_enc: Iterable[float],
    angles_cam: Iterable[float],
) -> float:
    """Calculate Mean Absolute Error (MAE) between encoder and camera measurements.

    Args:
        angles_enc: Sequence of angles measured by the wearable encoder.
        angles_cam: Sequence of angles measured by the optical camera system.

    Returns:
        MAE value in degrees.
    """
    enc = list(angles_enc)
    cam = list(angles_cam)
    if len(enc) != len(cam):
        raise ValueError("Data sequences must have identical lengths.")
    if not enc:
        return 0.0

    absolute_errors = [abs(e - c) for e, c in zip(enc, cam)]
    return sum(absolute_errors) / len(absolute_errors)


def generate_synthetic_telemetry(
    num_samples: int = 100,
    max_angle: float = 90.0,
    ppr: float = 600.0,
) -> List[Tuple[float, float, float]]:
    """Generate simulated knee flexion trajectory for testing and calibration.

    Simulates a squat or leg extension movement following a sinusoidal pattern:
    theta(t) = (max_angle / 2) * (1 - cos(2 * pi * t / T))

    Args:
        num_samples: Number of telemetry samples to produce.
        max_angle: Peak knee flexion angle in degrees (e.g. 90.0).
        ppr: Pulses Per Revolution for mock pulse generation.

    Returns:
        List of tuples: (timestamp_sec, simulated_angle_deg, simulated_pulses)
    """
    trajectory = []
    sampling_period = 0.02  # 50 Hz streaming simulation

    for i in range(num_samples):
        timestamp = i * sampling_period
        phase = (2.0 * math.pi * i) / float(max_angle if max_angle > 0 else 1)
        angle = (max_angle / 2.0) * (1.0 - math.cos(phase))
        pulses = (angle / 360.0) * ppr
        trajectory.append((round(timestamp, 4), round(angle, 2), round(pulses, 1)))

    return trajectory
