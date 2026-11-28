"""
Simulation Renderer Module — 2D Kinematic Skeleton & HUD Overlay

Renders real-time 2D schematic bone segments, joint highlights,
angular flexion arcs, and transparent HUD panels onto video frames.

Project Team: Ibrahim Halil Dogan, Mert Canoglu, Cem Baygin, Cansu Bulut
"""

from typing import Dict, Tuple
import cv2
import numpy as np


class SimulationRenderer:
    """
    Renders 2D schematic kinematic lower-limb visualization and HUD overlay.
    """

    COLOR_BONE = (0, 255, 128)        # Green: bone segments
    COLOR_JOINT = (0, 165, 255)       # Orange: joint centers
    COLOR_ARC = (255, 255, 0)         # Cyan: angular arc
    COLOR_TEXT = (255, 255, 255)      # White: HUD text
    COLOR_PANEL_BG = (40, 40, 40)     # Dark Gray: HUD panel background

    def __init__(
        self,
        bone_thickness: int = 3,
        joint_radius: int = 6,
        panel_alpha: float = 0.7,
    ) -> None:
        self.bone_thickness = bone_thickness
        self.joint_radius = joint_radius
        self.panel_alpha = panel_alpha

    def draw_skeleton_overlay(
        self,
        frame: np.ndarray,
        landmarks: Dict[str, Tuple[int, int]],
    ) -> np.ndarray:
        """
        Draws line segments connecting Hip -> Knee and Knee -> Ankle.
        """
        if "hip" in landmarks and "knee" in landmarks:
            cv2.line(frame, landmarks["hip"], landmarks["knee"], self.COLOR_BONE, self.bone_thickness)
        if "knee" in landmarks and "ankle" in landmarks:
            cv2.line(frame, landmarks["knee"], landmarks["ankle"], self.COLOR_BONE, self.bone_thickness)

        for pt in landmarks.values():
            cv2.circle(frame, pt, self.joint_radius, self.COLOR_JOINT, -1)

        return frame

    def draw_angle_arc(
        self,
        frame: np.ndarray,
        knee_point: Tuple[int, int],
        angle: float,
    ) -> np.ndarray:
        """
        Draws an angular arc centered at the knee joint indicating flexion.
        """
        cv2.putText(
            frame,
            f"{angle:.1f} deg",
            (knee_point[0] + 15, knee_point[1] - 10),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.6,
            self.COLOR_ARC,
            2,
        )
        return frame

    def draw_info_panel(
        self,
        frame: np.ndarray,
        angle: float,
        visibility: float,
        fps: float,
    ) -> np.ndarray:
        """
        Overlays a semi-transparent HUD telemetry panel in the upper-right corner.
        """
        h, w, _ = frame.shape
        panel_w, panel_h = 240, 100
        x1, y1 = w - panel_w - 20, 20
        x2, y2 = w - 20, y1 + panel_h

        overlay = frame.copy()
        cv2.rectangle(overlay, (x1, y1), (x2, y2), self.COLOR_PANEL_BG, -1)
        cv2.addWeighted(overlay, self.panel_alpha, frame, 1 - self.panel_alpha, 0, frame)

        cv2.putText(frame, f"Knee Angle: {angle:.1f} deg", (x1 + 12, y1 + 30),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.55, self.COLOR_TEXT, 1)
        cv2.putText(frame, f"Visibility: {visibility:.2f}", (x1 + 12, y1 + 55),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.55, self.COLOR_TEXT, 1)
        cv2.putText(frame, f"Process FPS: {fps:.1f}", (x1 + 12, y1 + 80),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.55, self.COLOR_TEXT, 1)

        return frame
