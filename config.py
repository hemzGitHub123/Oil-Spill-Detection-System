"""
config.py
Central configuration for the Black Oil Detection pipeline.

These defaults were derived by sampling actual pixel values from a real
sample video (oil entering muddy water):

    Region              Hue (OpenCV 0-179)   Saturation
    Oil (several spots)   ~100 - 107            ~35 - 60
    Muddy water           ~13 - 20              ~25 - 75
    Sky / horizon glare    unstable/random       ~2  - 8   (near greyscale)

Oil reflects the sky, so it comes out as a cool blue-grey hue. Muddy
water is a warm brown hue. That ~85 degree gap holds true at almost any
brightness, which is why HUE (not darkness, not smoothness) is the
primary signal here. Glare is rejected mainly by its very low, unstable
saturation rather than by hue.
"""

from dataclasses import dataclass, field
from typing import List, Tuple


@dataclass
class Config:
    # ---------- Input / Output ----------
    # EDIT THESE TWO PATHS for your own video.
    input_video_path: str = r"C:\Users\Hema\Downloads\spills\oil_spill_detector_v2\oil_spill_v2\input\spill9.mp4"
    output_video_path: str = r"C:\Users\Hema\Downloads\spills\oil_spill_detector_v2\oil_spill_v2\output\out9.mp4"

    # ---------- Region of Interest ----------
    # Polygon (list of x,y points) marking ONLY the water surface.
    # Excluding sky/horizon removes a lot of glare-driven noise before
    # any pixel math runs. Leave empty to use the full frame.
    roi_polygon: List[Tuple[int, int]] = field(default_factory=list)

    # ---------- Oil hue/saturation gate (PRIMARY cue) ----------
    oil_hue_min: int = 85          # cool blue-grey band start
    oil_hue_max: int = 130         # cool blue-grey band end
    oil_sat_min: int = 25          # rejects near-greyscale glare/horizon noise
    oil_val_max: int = 220         # reject very bright specular glare / white reflections

    # ---------- Blob filtering ----------
    min_blob_area: int = 80        # px; ignore tiny specks/noise while still catching small oil patches
    morph_kernel: int = 5          # open+close kernel to clean the mask / fill
                                    # small holes left by bright specular glints (reduced to preserve small features)

    # ---------- Temporal confirmation ----------
    # Cheap insurance against a single noisy frame, without adding much
    # lag (oil hue is already a strong, low-noise signal in practice).
    persistence_frames: int = 4         # must survive this many consecutive frames
    growth_ratio_thresh: float = 0.95   # must not shrink between first sight and now
    track_match_iou: float = 0.2        # min overlap to treat as "same" blob next frame
    max_missed_frames: int = 4          # frames a track can vanish before being dropped

    # ---------- Visualization ----------
    mask_color_bgr: Tuple[int, int, int] = (0, 0, 255)   # red tint fill
    outline_color_bgr: Tuple[int, int, int] = (0, 255, 255)  # yellow outline
    mask_alpha: float = 0.40
    font_scale: float = 0.8
