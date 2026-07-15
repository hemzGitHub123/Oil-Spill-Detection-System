"""
visualizer.py
Draws the result: a tinted fill + outline over each confirmed oil
region, a small "OIL" label at its centroid, and an overall status line
with the total oil coverage percentage.
"""

import cv2
import numpy as np


def annotate_frame(frame, confirmed_contours, cfg):
    h, w = frame.shape[:2]
    display = frame.copy()

    if confirmed_contours:
        overlay = display.copy()
        cv2.drawContours(overlay, confirmed_contours, -1, cfg.mask_color_bgr, thickness=cv2.FILLED)
        display = cv2.addWeighted(overlay, cfg.mask_alpha, display, 1 - cfg.mask_alpha, 0)
        cv2.drawContours(display, confirmed_contours, -1, cfg.outline_color_bgr, thickness=2)

        total_area = 0
        for c in confirmed_contours:
            area = cv2.contourArea(c)
            total_area += area
            M = cv2.moments(c)
            if M["m00"] > 0:
                cx = int(M["m10"] / M["m00"])
                cy = int(M["m01"] / M["m00"])
                cv2.putText(display, "OIL", (cx - 20, cy), cv2.FONT_HERSHEY_SIMPLEX,
                            cfg.font_scale, (0, 255, 255), 2, cv2.LINE_AA)

        coverage_pct = 100.0 * total_area / (h * w)
        status_text = f"OIL SPILL DETECTED  ({coverage_pct:.1f}% of frame)"
        status_color = (0, 0, 255)
    else:
        status_text = "MONITORING - NO OIL"
        status_color = (0, 200, 0)

    cv2.putText(display, status_text, (15, 30), cv2.FONT_HERSHEY_SIMPLEX,
                cfg.font_scale, status_color, 2, cv2.LINE_AA)
    return display
