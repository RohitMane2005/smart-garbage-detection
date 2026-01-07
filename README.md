# 🚯 Smart Garbage Detection System (AI + Computer Vision)

An AI-powered system that detects **littering events** from video footage using **YOLOv8**, **OpenCV**, and **Python**, and provides a simple **web dashboard** to upload videos and review detected events.

This project aims to improve civic cleanliness by identifying people **throwing garbage** in public areas using computer vision.

---

## 🧠 Problem Statement

Garbage littering in public places is a major civic issue. Manual monitoring is inefficient and costly.

**Goal:**  
Automatically detect when a **person throws garbage** using CCTV / video footage and capture evidence images.

---

## ✨ Features

- 🎯 Person detection using YOLOv8
- 🗑️ Garbage object detection (bottle, cup, paper, etc.)
- 🧍‍♂️ Person + garbage proximity logic
- 📸 Auto-save image only when **littering is detected**
- ⏱️ Cooldown mechanism to avoid duplicate events
- 🌐 Web UI to upload videos
- 🖼️ Event gallery to view detected images
- 🧪 Works on uploaded videos (not just static input)

---

## 🛠️ Tech Stack

### AI / Computer Vision
- Python
- OpenCV
- YOLOv8 (Ultralytics)

### Backend
- Flask (for UI & routing)
- Subprocess-based video processing

### Frontend
- HTML
- CSS
- JavaScript (basic)

---

## 📂 Project Structure
<pre>
ai-models/
├── src/
│ ├── main.py
│ ├── detectors/
│ │ ├── person_detector.py
│ │ ├── garbage_detector.py
│ │ └── littering_detector.py
│ └── utils/
│ ├── config.py
│ ├── video_utils.py
│ └── image_utils.py
│
├── web/
│ ├── app.py
│ ├── templates/
│ │ ├── upload.html
│ │ └── results.html
│ └── static/
│ └── css/
│
├── models/
│ └── yolov8n.pt
│
├── input_videos/
├── output_events/
│ └── images/
│
└── README.md
</pre>

yaml
Copy code

---

## ⚙️ Setup Instructions

### 1️⃣ Create Virtual Environment
```bash
python -m venv .venv
Activate:

bash
Copy code
.venv\Scripts\activate


2️⃣ Install Dependencies
bash
Copy code
pip install ultralytics opencv-python flask torch torchvision


3️⃣ Run Detection (CLI)
bash
Copy code
python src/main.py


4️⃣ Run Web Application
bash
Copy code
cd web
python app.py
Open browser:

cpp
Copy code
http://127.0.0.1:5000
🧪 How Littering Is Detected
A littering event is triggered when:

A person is detected

A new garbage object appears

Garbage is within proximity of the person

Cooldown ensures no duplicate captures

📸 Only then is the full frame saved.
