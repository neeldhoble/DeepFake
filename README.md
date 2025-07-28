
# DeepFake Detection Firewall 🚫🎥

> Detect and block deepfake images and videos using Python, OpenCV, and AI models.

## Features

- **Image detection**: Check if an uploaded image is a deepfake.
- **Video analysis**: Scan videos frame-by-frame for manipulations.
- **Pre-trained model support**: Based on XceptionNet, MesoNet, or similar.
- **OpenCV integration**: Face detection, preprocessing, visualization.
- **Backend API**: Built with FastAPI (or Flask) serving upload and detection endpoints.
- **Future UI support**: React-based frontend or simple HTML forms for uploads.
- **Logging & storage**: MongoDB or SQLite to track uploads and results.

## Table of Contents

- [Installation](#installation)  
- [Usage](#usage)  
- [Model & Training](#model--training)  
- [Project Structure](#project-structure)  
- [API Reference](#api-reference)  
- [Roadmap](#roadmap)  
- [Contributing](#contributing)  
- [License](#license)

---

## Installation

1. **Clone the repo**  
   ```bash
   git clone https://github.com/neeldhoble/DeepFake.git
   cd DeepFake
   ```

2. **Set up environment**  
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   pip install -r requirements.txt
   ```

3. **Download model weights**  
   Place your `.pth` or `.h5` model file in `backend/model_weights/`.

---

## Usage

- **Start the backend server**:
  ```bash
  cd backend
  uvicorn main:app --reload
  ```
- **Endpoints**:
  - `POST /detect/image` – Upload an image file for detection.
  - `POST /detect/video` – Upload a video for frame-by-frame analysis.

Sample response:
```json
{
  "is_deepfake": true,
  "confidence": 0.94,
  "processed_frames": 230
}
```

---

## Model & Training

This project assumes you have a pretrained deepfake detection model. Recommended options:
- **XceptionNet** pretrained on FaceForensics++ or DFDC dataset.
- **MesoNet** (Meso-4, MesoInception4) – lightweight alternative.

Training can be done in the `notebooks/` directory (e.g., `model_training.ipynb`).

---

## Project Structure

```
DeepFake/
├── backend/
│   ├── main.py
│   ├── detector/
│   │   ├── image_detector.py
│   │   ├── video_detector.py
│   │   └── model_loader.py
│   ├── utils/
│   │   ├── image_utils.py
│   │   └── video_utils.py
│   └── model_weights/
│       └── your_model.pth
├── frontend/           # Optional UI (React, Streamlit, or HTML)
├── notebooks/          # Training/testing experiments
├── tests/              # Unit tests
├── requirements.txt
├── Dockerfile
└── README.md
```

---

## API Reference

### `POST /detect/image`
- **Input**: JPEG/PNG image  
- **Output**: JSON with `is_deepfake`, `confidence`, `face_boxes`, etc.

### `POST /detect/video`
- **Input**: MP4 / AVI video file  
- **Behavior**: Extract frames, detect, summarize results  
- **Output**: JSON with overall `label`, `confidence`, and `frame_summary`.

---

## Roadmap

- 📊 Add frontend UI (React/Streamlit) with real-time feedback  
- 🌡️ Support Grad‑CAM to overlay fake-region heatmaps  
- 📁 Batch processing and multi-file support  
- 🧪 Add more detection models (e.g. EfficientNet, ViT)  
- 🗃️ Dashboard with logs, stats, and user authentication

---

## Contributing

Contributions are welcome! Please:
1. Fork the repo
2. Create a feature branch (`git checkout -b feature-xyz`)
3. Commit your changes (`git commit -m "Add XYZ"`)
4. Push and open a Pull Request

---

## License

This project is licensed under the **MIT License** – see the [LICENSE](LICENSE) file for details.
