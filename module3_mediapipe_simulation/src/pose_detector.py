"""
Pose Detector Module — Google MediaPipe Pose Wrapper

Wraps Google MediaPipe Pose (BlazePose) to extract lower-extremity
anatomical landmarks (hip, knee, ankle) and evaluate visibility thresholds.

Project Team: Ibrahim Halil Dogan, Mert Canoglu, Cem Baygin, Cansu Bulut
"""

from dataclasses import dataclass
from typing import Tuple, Optional, Any
import numpy as np


@dataclass
class LandmarkPoint:
    """Represents a 2D normalized anatomical landmark with confidence score."""
    x: float
    y: float
    visibility: float


class PoseDetector:
    """
    MediaPipe Pose inference wrapper for sagittal lower-limb kinematic tracking.
    """

    LANDMARK_LEFT_HIP = 23
    LANDMARK_RIGHT_HIP = 24
    LANDMARK_LEFT_KNEE = 25
    LANDMARK_RIGHT_KNEE = 26
    LANDMARK_LEFT_ANKLE = 27
    LANDMARK_RIGHT_ANKLE = 28

    def __init__(
        self,
        min_detection_confidence: float = 0.5,
        min_tracking_confidence: float = 0.5,
    ) -> None:
        self.min_detection_confidence = min_detection_confidence
        self.min_tracking_confidence = min_tracking_confidence
        self._pose = None
        # TODO: Initialize mp.solutions.pose.Pose(static_image_mode=False, model_complexity=1)

    def detect_landmarks(self, frame_bgr: np.ndarray) -> Optional[Any]:
        """
        Processes a BGR video frame and extracts full-body pose landmarks.

        TODO:
        - Convert BGR frame to RGB via cv2.cvtColor
        - Run self._pose.process(frame_rgb)
        - Return results.pose_landmarks if detected, None otherwise
        """
        return None

    def get_knee_landmarks(
        self,
        landmarks: Any,
        side: str = "left",
    ) -> Tuple[LandmarkPoint, LandmarkPoint, LandmarkPoint]:
        """
        Extracts Hip, Knee, and Ankle landmarks for the specified side.

        Args:
            landmarks: MediaPipe Pose landmark collection.
            side: Target limb side ('left' or 'right').

        Returns:
            Tuple of (hip, knee, ankle) LandmarkPoint instances.
        """
        if side.lower() == "left":
            hip_idx, knee_idx, ankle_idx = (
                self.LANDMARK_LEFT_HIP,
                self.LANDMARK_LEFT_KNEE,
                self.LANDMARK_LEFT_ANKLE,
            )
        elif side.lower() == "right":
            hip_idx, knee_idx, ankle_idx = (
                self.LANDMARK_RIGHT_HIP,
                self.LANDMARK_RIGHT_KNEE,
                self.LANDMARK_RIGHT_ANKLE,
            )
        else:
            raise ValueError(f"Invalid side '{side}'. Must be 'left' or 'right'.")

        # TODO: Access landmark coordinates and build LandmarkPoint objects
        return (
            LandmarkPoint(0.0, 0.0, 0.0),
            LandmarkPoint(0.0, 0.0, 0.0),
            LandmarkPoint(0.0, 0.0, 0.0),
        )

    def check_visibility(
        self,
        landmarks: Tuple[LandmarkPoint, ...],
        threshold: float = 0.6,
    ) -> bool:
        """
        Checks whether all specified landmarks satisfy minimum visibility confidence.

        Returns:
            True if all landmarks exceed threshold, False otherwise.
        """
        return all(lm.visibility >= threshold for lm in landmarks)
