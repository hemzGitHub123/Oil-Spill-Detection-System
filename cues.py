"""
cues.py
Per-pixel oil cue.

Oil floating on muddy water reflects the sky/ambient light, giving it a
cool blue-grey hue, while the muddy water itself is a warm brown hue -
a gap of roughly 85 degrees on the OpenCV 0-179 hue scale. This holds
true across a wide brightness range (unlike a darkness-based cue) and
across different amounts of surface shimmer (unlike a smoothness-based
cue), which is why it's used as the primary, near-standalone gate here.

Sky glare / horizon reflections are rejected mainly via the saturation
floor: glare is close to greyscale (very low, noisy saturation), while
oil keeps a moderate, fairly consistent saturation even when its hue
is the same ballpark as a blue sky reflection.
"""

import cv2
import numpy as np


def oil_hue_mask(hsv_frame: np.ndarray, cfg) -> np.ndarray:
    h = hsv_frame[:, :, 0]
    s = hsv_frame[:, :, 1]
    v = hsv_frame[:, :, 2]

    hue_ok = (h >= cfg.oil_hue_min) & (h <= cfg.oil_hue_max)
    sat_ok = s >= cfg.oil_sat_min
    val_ok = v <= cfg.oil_val_max

    mask = (hue_ok & sat_ok & val_ok).astype(np.uint8) * 255
    return mask
