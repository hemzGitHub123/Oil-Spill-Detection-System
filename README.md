<img width="930" height="395" alt="Screenshot 2026-07-15 083424" src="https://github.com/user-attachments/assets/8a39054c-b099-4f0c-8659-579e7e8e57af" /># 🌊 Oil Spill Detection System

> **A Computer Vision-based system for detecting oil spills in muddy flowing water using CCTV video streams.**

![Python](https://img.shields.io/badge/Python-3.x-blue?logo=python)
![OpenCV](https://img.shields.io/badge/OpenCV-Computer%20Vision-green)
![Status](https://img.shields.io/badge/Status-Completed-success)

---

# 📖 Overview

Oil spill detection is an important task in environmental monitoring and industrial safety. Detecting oil spills in muddy flowing water is particularly challenging because oil continuously changes shape and appearance while reflections, ripples, and varying lighting conditions often resemble oil.

This project presents a **Computer Vision-based Oil Spill Detection System** that processes CCTV video streams to identify floating oil spill regions. Instead of relying on deep learning object detection models, the system uses **HSV color analysis**, **Region of Interest (ROI) masking**, **morphological image processing**, **contour detection**, and **temporal filtering** to achieve stable and reliable oil spill detection.

The project was developed to provide an efficient and lightweight solution suitable for real-time monitoring.

---

# 🎯 Objectives

- Detect floating oil spills from CCTV surveillance footage.
- Differentiate oil spills from muddy water.
- Reduce false detections caused by ripples and reflections.
- Perform real-time video processing.
- Visualize detected oil spill regions with bounding contours.

---

# ✨ Key Features

- Real-time video processing
- HSV color space analysis
- Hue and Saturation-based oil detection
- Region of Interest (ROI) masking
- Morphological noise removal
- Contour extraction and visualization
- Temporal filtering for stable detection
- Configurable detection thresholds
- Modular project architecture

---

# 🏗 Detection Pipeline

```text
Input CCTV Video
        │
        ▼
Frame Extraction
        │
        ▼
HSV Color Conversion
        │
        ▼
Hue & Saturation Analysis
        │
        ▼
Region of Interest (ROI)
        │
        ▼
Morphological Processing
        │
        ▼
Contour Detection
        │
        ▼
Temporal Consistency Filtering
        │
        ▼
Oil Spill Visualization
```

---

# 🛠 Technology Stack

| Category | Technologies |
|----------|--------------|
| Programming Language | Python |
| Computer Vision | OpenCV |
| Numerical Computing | NumPy |

---

# 📂 Project Structure

```text
Oil-Spill-Detection-System/
│
├── config.py         # Configuration parameters
├── cues.py           # HSV-based oil detection logic
├── detector.py       # ROI masking and contour detection
├── temporal.py       # Temporal filtering
├── visualizer.py     # Detection visualization
├── main.py           # Main application
│
├── input/            # Input videos
├── output/           # Output videos
│
├── requirements.txt
├── README.md
└── .gitignore
```

---

# 🚀 Installation

Clone the repository

```bash
git clone https://github.com/hemzGitHub123/Oil-Spill-Detection-System.git
```

Navigate to the project

```bash
cd Oil-Spill-Detection-System
```

Install dependencies

```bash
pip install -r requirements.txt
```

---

# ▶️ Usage

Update the input and output paths inside **config.py**

```python
input_video_path = "input/sample.mp4"
output_video_path = "output/result.mp4"
```

Run the project

```bash
python main.py
```

Or use command-line arguments

```bash
python main.py --source input/sample.mp4 --output output/result.mp4
```

# ⚠ Challenges Addressed

The system addresses several practical challenges encountered in oil spill detection:

- Oil has irregular and continuously changing shapes.
- Muddy water produces textures similar to oil.
- Water ripples introduce false detections.
- Reflections from the sky affect appearance.
- Lighting conditions vary throughout the video.

The implemented pipeline combines multiple computer vision techniques to improve detection stability while maintaining computational efficiency.

---

# 🌍 Applications

- Environmental Monitoring
- Industrial Water Surveillance
- Oil Refinery Monitoring
- Water Pollution Detection
- Smart CCTV Surveillance
- Industrial Safety Systems

---

# 🔮 Future Improvements

- Deep Learning-based Semantic Segmentation (U-Net / DeepLabV3+)
- Edge AI Deployment
- Automatic Alert System
- Multi-camera Monitoring
- Cloud Dashboard Integration
- Performance Optimization for High-Resolution Videos

---

# 👩‍💻 Author

**Hemalatha M**

AI Developer | Machine Learning Engineer | Computer Vision Engineer

---

# ⭐ Support

If you found this project useful, consider giving it a ⭐ on GitHub.
