"""Computer Vision & Pose Estimation Module (Module 3).

Computes lower-limb 2D vector kinematics (knee flexion and ankle angles)
from optical landmark coordinates (Hip, Knee, Ankle, Foot) based on the
vector dot product formulation in Proposal Section 2.2.2.
"""

from typing import Tuple
import math

Point2D = Tuple[float, float]


def calculate_vector_angle(v1: Tuple[float, float], v2: Tuple[float, float]) -> float:
    """Calculate the interior angle between two 2D vectors in degrees.

    Formula:
        theta = arccos( (v1 . v2) / (||v1|| * ||v2||) ) * (180 / pi)

    Args:
        v1: First 2D vector (x, y).
        v2: Second 2D vector (x, y).

    Returns:
        Angle in degrees in the range [0.0, 180.0].
    """
    dot_product = (v1[0] * v2[0]) + (v1[1] * v2[1])
    norm_v1 = math.hypot(v1[0], v1[1])
    norm_v2 = math.hypot(v2[0], v2[1])

    if norm_v1 == 0.0 or norm_v2 == 0.0:
        return 0.0

    cosine = dot_product / (norm_v1 * norm_v2)
    # Clamp cosine to [-1.0, 1.0] to safeguard against floating-point inaccuracies
    cosine = max(-1.0, min(1.0, cosine))

    return math.degrees(math.acos(cosine))


def calculate_knee_angle(
    hip: Point2D,
    knee: Point2D,
    ankle: Point2D,
) -> float:
    """Calculate vision-based knee flexion angle from sagittal anatomical landmarks.

    Formulation:
        u = P_hip - P_knee
        v = P_ankle - P_knee
        theta_knee,cam = arccos( (u . v) / (||u|| * ||v||) ) * (180 / pi)

    Args:
        hip: (x, y) coordinates of the hip landmark.
        knee: (x, y) coordinates of the knee landmark.
        ankle: (x, y) coordinates of the ankle landmark.

    Returns:
        Knee angle in degrees.
    """
    u = (hip[0] - knee[0], hip[1] - knee[1])
    v = (ankle[0] - knee[0], ankle[1] - knee[1])
    return calculate_vector_angle(u, v)


def calculate_ankle_angle(
    knee: Point2D,
    ankle: Point2D,
    foot: Point2D,
) -> float:
    """Calculate vision-based ankle joint angle (dorsiflexion / plantarflexion).

    Formulation:
        -v = P_knee - P_ankle
        w = P_foot - P_ankle
        theta_ankle,cam = arccos( (-v . w) / (||-v|| * ||w||) ) * (180 / pi)

    Args:
        knee: (x, y) coordinates of the knee landmark.
        ankle: (x, y) coordinates of the ankle landmark.
        foot: (x, y) coordinates of the foot index landmark.

    Returns:
        Ankle angle in degrees.
    """
    neg_v = (knee[0] - ankle[0], knee[1] - ankle[1])
    w = (foot[0] - ankle[0], foot[1] - ankle[1])
    return calculate_vector_angle(neg_v, w)
