# 🌊 Oil Spill Detection System

> **An AI-powered Computer Vision system for detecting oil spills in muddy flowing water using CCTV surveillance footage.**

# 📖 Overview

Oil spill detection is essential for protecting water resources and ensuring industrial environmental safety. Conventional monitoring methods rely on manual inspection, making them time-consuming, expensive, and prone to human error.

This project presents a **Computer Vision and Machine Learning-based Oil Spill Detection System** capable of detecting floating oil spills from **CCTV video streams captured over muddy flowing water**.

Unlike traditional object detection problems, oil spills do not have fixed shapes, sizes, or appearances. To overcome this challenge, the system combines advanced image processing techniques with machine learning to accurately distinguish oil spill regions from muddy water while minimizing false detections caused by ripples, reflections, and lighting variations.

---

# 🎯 Project Objectives

- Detect floating oil spills from CCTV footage.
- Differentiate oil from muddy water under varying lighting conditions.
- Reduce false positives caused by water ripples and reflections.
- Build a robust and efficient real-time detection pipeline.
- Provide visual alerts for detected oil spill regions.

---

# ✨ Key Highlights

✔ Real-time oil spill detection from surveillance videos.

✔ Designed specifically for challenging muddy water environments.

✔ Image enhancement using **CLAHE** for improved visibility.

✔ Motion analysis using **Dense Optical Flow**.

✔ Texture extraction using **Local Binary Pattern (LBP)**.

✔ Multi-scale texture analysis using **Wavelet Transform**.

✔ Machine Learning-based classification using **XGBoost**.

✔ Morphological refinement for noise removal.

✔ Bounding-box visualization of detected oil regions.

✔ Configurable detection parameters for different environments.

✔ Modular architecture for easy maintenance and future upgrades.

---

# 🏗 Detection Pipeline

```text
CCTV Video
      │
      ▼
Video Frame Extraction
      │
      ▼
Image Enhancement (CLAHE)
      │
      ▼
Noise Reduction
      │
      ▼
Feature Extraction
 ├── Local Binary Pattern (LBP)
 ├── Dense Optical Flow
 └── Wavelet Features
      │
      ▼
Feature Fusion
      │
      ▼
Machine Learning Classification
      │
      ▼
Morphological Refinement
      │
      ▼
Oil Spill Detection & Visualization
```

---

# 🛠 Tech Stack

| Category | Technologies |
|----------|--------------|
| Programming Language | Python |
| Computer Vision | OpenCV |
| Machine Learning | XGBoost, Scikit-learn |
| Numerical Computing | NumPy |
| Image Processing | CLAHE, LBP, Wavelet Transform |
| Visualization | OpenCV |

---

# 🚀 Features

- Real-time video processing
- CCTV-based oil spill monitoring
- High accuracy in muddy water conditions
- Robust against water ripples
- Bounding box visualization
- Easy parameter configuration
- Lightweight and efficient implementation
- Modular project architecture

---

# 📂 Project Structure

```text
Oil-Spill-Detection-System/
│
├── config.py
├── cues.py
├── detector.py
├── temporal.py
├── visualizer.py
├── main.py
│
├── input/
├── output/
│
├── requirements.txt
├── README.md
└── .gitignore
```

---

# 📊 Challenges Addressed

One of the major challenges in this project was that oil spills:

- Have irregular and continuously changing shapes.
- Reflect surrounding light, making them difficult to distinguish.
- Blend with muddy water textures.
- Produce different appearances under varying environmental conditions.
- Can be confused with water ripples and surface reflections.

To address these challenges, the system combines multiple computer vision techniques instead of relying solely on object detection models.

---

# 📈 Applications

- Environmental Monitoring
- Oil Refineries
- Industrial Wastewater Monitoring
- Smart City Surveillance
- Water Pollution Detection
- Industrial Safety Systems

---

# 🔮 Future Improvements

- Semantic Segmentation using U-Net / DeepLabV3+
- Edge AI deployment (Jetson/Raspberry Pi)
- Cloud-based monitoring dashboard
- Automatic email/SMS alert system
- Multi-camera monitoring
- Deep Learning-based classification
- Temporal tracking for improved stability

---

# 👩‍💻 Author

**Hemalatha M**

AI Developer | Machine Learning Engineer | Computer Vision Engineer

---

⭐ If you found this project interesting, consider giving it a star on GitHub.
