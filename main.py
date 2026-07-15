"""
main.py
Black-oil-in-muddy-water detection for a fixed CCTV camera.

============================================================
 EDIT YOUR INPUT / OUTPUT VIDEO PATHS IN config.py:
     input_video_path  = "..."
     output_video_path = "..."
 (You can also override them on the command line, see below.)
============================================================

Run:
    python main.py
    python main.py --source path/to/video.mp4 --output path/to/result.mp4
    python main.py --source 0            # webcam / live CCTV index
    python main.py --source rtsp://...   # IP camera stream

Press 'q' to quit the preview window early. The output video is saved
incrementally as frames are processed either way.
"""

import argparse
import cv2

from config import Config
from detector import build_roi_mask, compute_candidate_mask, extract_blobs
from temporal import TrackManager
from visualizer import annotate_frame


def main():
    cfg = Config()

    parser = argparse.ArgumentParser()
    parser.add_argument("--source", default=cfg.input_video_path,
                         help="Video file path, camera index, or RTSP URL")
    parser.add_argument("--output", default=cfg.output_video_path,
                         help="Path to save the annotated output video")
    parser.add_argument("--no-preview", action="store_true",
                         help="Don't open a live preview window (still saves output video)")
    args = parser.parse_args()

    source = args.source
    if str(source).isdigit():
        source = int(source)

    cap = cv2.VideoCapture(source)
    if not cap.isOpened():
        raise RuntimeError(f"Could not open video source: {source}")

    fps = cap.get(cv2.CAP_PROP_FPS) or 24.0
    width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

    fourcc = cv2.VideoWriter_fourcc(*"mp4v")
    writer = cv2.VideoWriter(args.output, fourcc, fps, (width, height))
    if not writer.isOpened():
        raise RuntimeError(f"Could not open output video for writing: {args.output}")

    tracker = TrackManager(cfg)
    roi_mask = None
    frame_idx = 0

    while True:
        ret, frame = cap.read()
        if not ret:
            break
        frame_idx += 1

        if roi_mask is None:
            roi_mask = build_roi_mask(frame.shape, cfg.roi_polygon)

        candidate_mask = compute_candidate_mask(frame, cfg, roi_mask)
        blobs = extract_blobs(candidate_mask, cfg.min_blob_area)
        confirmed_tracks, bbox_to_contour = tracker.update(blobs, frame_idx)

        confirmed_contours = [
            bbox_to_contour[t.bbox] for t in confirmed_tracks if t.bbox in bbox_to_contour
        ]

        display = annotate_frame(frame, confirmed_contours, cfg)
        writer.write(display)

        if not args.no_preview:
            cv2.imshow("Oil Spill Detection", display)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

    cap.release()
    writer.release()
    cv2.destroyAllWindows()
    print(f"Done. Annotated video saved to: {args.output}")


if __name__ == "__main__":
    main()
