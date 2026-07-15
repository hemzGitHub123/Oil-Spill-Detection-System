# Black Oil Detection — v2 (rewritten around your real footage)

## What changed from v1, and why
v1 failed to detect oil at all because it required oil to be *darker*
and *smoother* than the water. Your actual oil is glossy/reflective
with bright specular streaks, so neither assumption held — measuring
real pixels from `spill3.mp4` showed oil brightness (V) actually
overlaps with plain water, and oil has just as much local texture
variance as ripples do (sometimes more, from the shine).

What I measured instead, directly from your video:

| Region                | Hue (0-179) | Saturation |
|------------------------|-------------|------------|
| Oil (multiple spots)   | ~100-107    | ~35-60     |
| Muddy water            | ~13-20      | ~25-75     |
| Sky / horizon glare    | unstable    | ~2-8 (near greyscale) |

Oil reflects the sky → cool blue-grey hue. Muddy water is warm brown.
That ~85-90° hue gap holds at almost any brightness, which is why hue
(not darkness, not smoothness) is now the primary — almost sole — cue.
Glare is rejected by its very low, noisy saturation, not by hue.

Tested against the full 240-frame clip: 0% false positives on every
ripple-only frame, clean detection starting the frame oil enters
(frame 87), continuous correct annotation through to the end.

## EDIT YOUR PATHS HERE
Open `config.py`, top of the file:
```python
input_video_path: str = "/mnt/user-data/uploads/spill3.mp4"
output_video_path: str = "/mnt/user-data/outputs/spill3_annotated.mp4"
```
Or override on the command line:
```
python main.py --source your_video.mp4 --output your_result.mp4
```

## Run it
```
pip install -r requirements.txt
python main.py                     # uses paths from config.py, shows live preview
python main.py --no-preview        # just processes and saves, no window
python main.py --source 0          # webcam / camera index instead of a file
```
The output video is saved with the oil region tinted red, outlined in
yellow, labeled "OIL", and a status line showing live oil coverage %.

## Files
- `config.py` — input/output paths + every tunable threshold
- `cues.py` — the oil hue/saturation gate (the core logic)
- `detector.py` — ROI masking, morphological cleanup, blob extraction
- `temporal.py` — light persistence check (anti-flicker insurance, not the main gate anymore)
- `visualizer.py` — tint + outline + "OIL" label + status line
- `main.py` — wires it together, reads input video, writes annotated output video

## If you test on a different video and it misses oil or over-detects
1. Sample a few clean oil pixels and clean water pixels yourself:
   ```python
   import cv2
   frame = cv2.imread('your_frame.jpg')
   hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
   print(hsv[y, x])   # H, S, V at a pixel you know is oil/water
   ```
2. Adjust `oil_hue_min` / `oil_hue_max` / `oil_sat_min` in `config.py`
   to bracket your oil's real hue/saturation, with water's values
   clearly outside that band.
3. Set `roi_polygon` to the water surface only if your camera angle
   shows a lot of sky/horizon.
