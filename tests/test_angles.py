"""Unit Tests for Lower-Limb Goniometer Kinematics and Optical Angle Math.

Module 5: Integration, CI/CD & Testing.
"""

import pytest
import math
from src.kinematics import (
    calculate_encoder_angle,
    calculate_dual_encoder_angle,
    calculate_rmse,
    calculate_mae,
    generate_synthetic_telemetry,
)
from src.vision_tracker import (
    calculate_vector_angle,
    calculate_knee_angle,
    calculate_ankle_angle,
)
from src.gui_app import GoniometerDashboard


def test_zero_angle():
    """Verify 0 pulses yields 0.0 degrees."""
    assert calculate_encoder_angle(0) == 0.0


def test_quarter_turn():
    """Verify 150 pulses on a 600 PPR encoder corresponds to a 90-degree right angle."""
    assert calculate_encoder_angle(150, 600) == 90.0


def test_full_turn():
    """Verify 600 pulses yields a complete 360-degree rotation."""
    assert calculate_encoder_angle(600, 600) == 360.0


def test_zero_ppr_raises_value_error():
    """Verify zero PPR guard raises ValueError."""
    with pytest.raises(ValueError):
        calculate_encoder_angle(100, ppr=0)


def test_dual_encoder_superposition():
    """Verify polycentric dual encoder equation: theta = theta_0 + k1*n1 + k2*n2."""
    # k1 = 360/600 = 0.6, k2 = 360/600 = 0.6
    # 75 pulses each -> (0.6 * 75) + (0.6 * 75) = 45 + 45 = 90 degrees
    angle = calculate_dual_encoder_angle(delta_n1=75, delta_n2=75, k1=0.6, k2=0.6, theta_0=0.0)
    assert pytest.approx(angle, rel=1e-5) == 90.0

    # With non-zero baseline offset
    angle_offset = calculate_dual_encoder_angle(delta_n1=75, delta_n2=75, k1=0.6, k2=0.6, theta_0=5.0)
    assert pytest.approx(angle_offset, rel=1e-5) == 95.0


def test_vector_angle_orthogonal():
    """Verify orthogonal vectors produce 90.0 degrees."""
    v1 = (1.0, 0.0)
    v2 = (0.0, 1.0)
    assert pytest.approx(calculate_vector_angle(v1, v2), rel=1e-5) == 90.0


def test_vector_angle_collinear():
    """Verify parallel vectors yield 0 degrees and anti-parallel yield 180 degrees."""
    v1 = (1.0, 0.0)
    v2 = (5.0, 0.0)
    assert pytest.approx(calculate_vector_angle(v1, v2), rel=1e-5) == 0.0

    v_opp = (-3.0, 0.0)
    assert pytest.approx(calculate_vector_angle(v1, v_opp), rel=1e-5) == 180.0


def test_knee_angle_calculation():
    """Verify sagittal hip-knee-ankle 90-degree flexion."""
    hip = (0.0, 1.0)
    knee = (0.0, 0.0)
    ankle = (1.0, 0.0)
    assert pytest.approx(calculate_knee_angle(hip, knee, ankle), rel=1e-5) == 90.0


def test_ankle_angle_calculation():
    """Verify sagittal knee-ankle-foot angle calculation."""
    knee = (0.0, 1.0)
    ankle = (0.0, 0.0)
    foot = (1.0, 0.0)
    assert pytest.approx(calculate_ankle_angle(knee, ankle, foot), rel=1e-5) == 90.0


def test_rmse_and_mae_calculation():
    """Verify error discrepancy metrics between encoder and camera streams."""
    enc = [90.0, 45.0, 30.0]
    cam = [92.0, 43.0, 30.0]

    # Errors: [2.0, -2.0, 0.0]
    # MAE = (2 + 2 + 0) / 3 = 1.3333...
    # RMSE = sqrt((4 + 4 + 0) / 3) = sqrt(8/3) ~= 1.63299
    expected_mae = 4.0 / 3.0
    expected_rmse = math.sqrt(8.0 / 3.0)

    assert pytest.approx(calculate_mae(enc, cam), rel=1e-4) == expected_mae
    assert pytest.approx(calculate_rmse(enc, cam), rel=1e-4) == expected_rmse


def test_synthetic_telemetry_generator():
    """Verify synthetic telemetry generates requested sample count and valid angles."""
    telemetry = generate_synthetic_telemetry(num_samples=50, max_angle=90.0)
    assert len(telemetry) == 50
    for ts, angle, pulses in telemetry:
        assert ts >= 0.0
        assert 0.0 <= angle <= 90.01
        assert pulses >= 0.0


def test_dashboard_calibration_and_metrics():
    """Verify GUI dashboard sliding window and re-zero calibration."""
    dashboard = GoniometerDashboard(buffer_size=5)
    for i in range(10):
        dashboard.add_synchronized_sample(timestamp=i * 0.1, angle_encoder=10.0 + i, angle_camera=10.0 + i)

    # Buffer should maintain last 5 samples
    assert len(dashboard.timestamps) == 5
    metrics = dashboard.get_realtime_metrics()
    assert metrics["rmse"] == 0.0
    assert metrics["mae"] == 0.0

    # Calibrate zero
    dashboard.calibrate_zero(reference_angle=0.0)
    assert dashboard.is_calibrated is True
