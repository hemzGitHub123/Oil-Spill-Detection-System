"""
detector.py
Per-frame detection pipeline: applies the ROI mask, runs the oil hue
gate, cleans the result morphologically, and extracts candidate blobs
to hand off to the temporal tracker.
"""

import cv2
import numpy as np

from cues import oil_hue_mask


def build_roi_mask(frame_shape, roi_polygon):
    """Builds a binary mask restricting detection to the water surface.
    If no polygon is given, the whole frame is used."""
    h, w = frame_shape[:2]
    if roi_polygon:
        mask = np.zeros((h, w), dtype=np.uint8)
        pts = np.array([roi_polygon], dtype=np.int32)
        cv2.fillPoly(mask, pts, 255)
    else:
        mask = np.full((h, w), 255, dtype=np.uint8)
    return mask


def compute_candidate_mask(frame_bgr, cfg, roi_mask):
    hsv = cv2.cvtColor(frame_bgr, cv2.COLOR_BGR2HSV)

    mask = oil_hue_mask(hsv, cfg)
    mask = cv2.bitwise_and(mask, roi_mask)

    # Morphological cleanup: close first to fill small holes left by
    # bright specular highlights inside an oil patch, then open to
    # drop leftover speckle noise.
    k = cfg.morph_kernel
    kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (k, k))
    mask = cv2.morphologyEx(mask, cv2.MORPH_CLOSE, kernel)
    mask = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel)

    return mask


def extract_blobs(mask, min_area):
    """Returns a list of (bbox, area, contour) for each surviving blob."""
    contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    blobs = []
    for c in contours:
        area = cv2.contourArea(c)
        if area < min_area:
            continue
        x, y, w, h = cv2.boundingRect(c)
        blobs.append(((x, y, w, h), area, c))
    return blobs
