"""
Camera Capture Module — Real-Time Video Ingestion

Manages monocular RGB video capture via OpenCV VideoCapture,
acquiring 1080p @ 30 FPS video frames in the sagittal plane
with microsecond monotonic timestamps.

Project Team: Ibrahim Halil Dogan, Mert Canoglu, Cem Baygin, Cansu Bulut
"""

import time
from typing import Tuple, Optional
import cv2
import numpy as np


class CameraCapture:
    """
    Video frame ingestion and monotonic timestamp management.
    """

    def __init__(
        self,
        camera_id: int = 0,
        width: int = 1920,
        height: int = 1080,
        fps: int = 30,
    ) -> None:
        self.camera_id = camera_id
        self.width = width
        self.height = height
        self.fps = fps
        self._capture: Optional[cv2.VideoCapture] = None
        self._start_time: float = 0.0
        self._frame_count: int = 0

    def start(self) -> bool:
        """
        Opens camera stream and applies resolution and frame rate properties.

        TODO:
        - Instantiate cv2.VideoCapture(self.camera_id)
        - Configure CAP_PROP_FRAME_WIDTH, CAP_PROP_FRAME_HEIGHT, CAP_PROP_FPS
        - Check if opened successfully, record start timestamp
        - Return True if active
        """
        self._capture = cv2.VideoCapture(self.camera_id)
        if not self._capture.isOpened():
            return False
        self._capture.set(cv2.CAP_PROP_FRAME_WIDTH, self.width)
        self._capture.set(cv2.CAP_PROP_FRAME_HEIGHT, self.height)
        self._capture.set(cv2.CAP_PROP_FPS, self.fps)
        self._start_time = time.perf_counter()
        return True

    def read_frame(self) -> Tuple[bool, Optional[np.ndarray], float]:
        """
        Reads a single frame from the camera stream.

        Returns:
            Tuple of (success, BGR frame array or None, timestamp_seconds).
        """
        if self._capture is None or not self._capture.isOpened():
            return False, None, 0.0

        success, frame = self._capture.read()
        timestamp = time.perf_counter()
        if success:
            self._frame_count += 1
        return success, frame, timestamp

    def stop(self) -> None:
        """Releases camera capture resources."""
        if self._capture and self._capture.isOpened():
            self._capture.release()
            self._capture = None

    def get_timestamp(self) -> float:
        """Returns current monotonic timestamp in seconds."""
        return time.perf_counter()
