"""
temporal.py
Tracks oil-candidate blobs across frames using simple IoU matching, and
requires a short persistence window before confirming a detection. With
hue as a strong, low-noise primary signal, this is cheap insurance
against a single stray frame rather than the main line of defense.
"""

import numpy as np


class Track:
    _next_id = 1

    def __init__(self, bbox, area, frame_idx):
        self.id = Track._next_id
        Track._next_id += 1
        self.bbox = bbox            # (x, y, w, h)
        self.first_area = area
        self.last_area = area
        self.first_frame = frame_idx
        self.last_seen = frame_idx
        self.hits = 1
        self.missed = 0
        self.confirmed = False

    def update(self, bbox, area, frame_idx):
        self.bbox = bbox
        self.last_area = area
        self.last_seen = frame_idx
        self.hits += 1
        self.missed = 0

    def growth_ratio(self):
        if self.first_area <= 0:
            return 0.0
        return self.last_area / self.first_area


def _iou(b1, b2):
    x1, y1, w1, h1 = b1
    x2, y2, w2, h2 = b2
    xa1, ya1, xa2, ya2 = x1, y1, x1 + w1, y1 + h1
    xb1, yb1, xb2, yb2 = x2, y2, x2 + w2, y2 + h2
    inter_x1, inter_y1 = max(xa1, xb1), max(ya1, yb1)
    inter_x2, inter_y2 = min(xa2, xb2), min(ya2, yb2)
    if inter_x2 <= inter_x1 or inter_y2 <= inter_y1:
        return 0.0
    inter = (inter_x2 - inter_x1) * (inter_y2 - inter_y1)
    union = w1 * h1 + w2 * h2 - inter
    return inter / union if union > 0 else 0.0


class TrackManager:
    def __init__(self, cfg):
        self.cfg = cfg
        self.tracks = []

    def update(self, blobs, frame_idx):
        """blobs: list of (bbox, area, contour). Returns (confirmed_tracks,
        bbox_to_contour) so the caller can recover contours for drawing."""
        bbox_to_contour = {b[0]: b[2] for b in blobs}

        unmatched_blobs = list(range(len(blobs)))
        unmatched_tracks = list(range(len(self.tracks)))

        matches = []
        for ti in list(unmatched_tracks):
            best_bi, best_iou = None, 0.0
            for bi in unmatched_blobs:
                iou = _iou(self.tracks[ti].bbox, blobs[bi][0])
                if iou > best_iou:
                    best_iou, best_bi = iou, bi
            if best_bi is not None and best_iou >= self.cfg.track_match_iou:
                matches.append((ti, best_bi))
                unmatched_blobs.remove(best_bi)
                unmatched_tracks.remove(ti)

        for ti, bi in matches:
            bbox, area, _ = blobs[bi]
            self.tracks[ti].update(bbox, area, frame_idx)

        for ti in unmatched_tracks:
            self.tracks[ti].missed += 1

        for bi in unmatched_blobs:
            bbox, area, _ = blobs[bi]
            self.tracks.append(Track(bbox, area, frame_idx))

        # Drop stale tracks that have vanished for too long.
        self.tracks = [t for t in self.tracks if t.missed <= self.cfg.max_missed_frames]

        confirmed = []
        for t in self.tracks:
            survived = (t.last_seen - t.first_frame) >= self.cfg.persistence_frames
            held = t.growth_ratio() >= self.cfg.growth_ratio_thresh
            if survived and held and t.missed == 0:
                t.confirmed = True
                confirmed.append(t)
        return confirmed, bbox_to_contour
