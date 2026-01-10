# 🚯 Smart Garbage Detection System  
### AI + Computer Vision for Littering Detection


::contentReference[oaicite:0]{index=0}


An **AI-powered video analytics system** that detects **littering events** from video footage using **YOLOv8**, **OpenCV**, and **Python**, with a lightweight **Flask-based web dashboard** for video upload and result visualization.

This project aims to improve **civic cleanliness** by automatically identifying people **throwing garbage in public areas** using computer vision.

---

## 🧠 Problem Statement

Garbage littering in public places is a major civic issue.  
Manual CCTV monitoring is:

- Inefficient  
- Costly  
- Not scalable  

### 🎯 Objective
Automatically detect **littering behavior** from CCTV or uploaded video footage and capture **evidence frames** using AI.

---

## ✨ Key Features

- 🎯 Person detection using **YOLOv8**
- 🗑️ Garbage object detection (bottle, cup, paper, etc.)
- 🧍‍♂️ Person + garbage **proximity-based logic**
- 📸 Auto-save image **only when littering is detected**
- ⏱️ Cooldown mechanism to avoid duplicate detections
- 🌐 Web UI to upload videos
- 🖼️ Results page with **event image gallery**
- 🧪 Works on **uploaded videos**, not just static inputs

---

## 🛠️ Tech Stack

### 🤖 AI / Computer Vision
- Python  
- OpenCV  
- YOLOv8 (Ultralytics)

### ⚙️ Backend
- Flask  
- Subprocess-based video processing  

### 🎨 Frontend
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

<pre>
### 1️⃣ Create Virtual Environment

python -m venv .venv
Activate:

bash
Copy code
.venv\Scripts\activate
2️⃣ Install Dependencies
bash
Copy code
pip install ultralytics opencv-python flask torch torchvision
3️⃣ Run Detection (CLI Mode)
bash
Copy code
python src/main.py
4️⃣ Run Web Application
bash
Copy code
cd web
python app.py
Open in browser:

cpp
Copy code
http://127.0.0.1:5000
🧪 How Littering Is Detected
A littering event is triggered only when all conditions are met:

👤 A person is detected

🗑️ A new garbage object appears

📏 Garbage is within a defined proximity of the person

⏱️ Cooldown timer prevents duplicate captures

📸 Only then is the full video frame saved as evidence.
</pre>

🏗️ System Architecture







mermaid
Copy code
flowchart TD
    A[User Uploads Video] --> B[Web Dashboard (Flask)]
    B --> C[Video Processing Engine]
    C --> D[YOLOv8 Object Detection]
    D --> D1[Person Detection]
    D --> D2[Garbage Detection]
    D1 --> E[Littering Logic Engine]
    D2 --> E
    E --> F[Event Triggered]
    F --> G[Save Evidence Frame]
    G --> H[Results Gallery UI]
🚀 Future Enhancements
📹 Live CCTV stream integration

📍 Timestamp & location overlay

🚨 Real-time alerts

📊 Analytics dashboard

🤖 Action recognition for higher accuracy

📌 Use Cases
Smart Cities

Municipal Corporations

Public Surveillance Systems

Cleanliness Monitoring Projects

⭐ Why This Project Matters
This project demonstrates:

Real-world AI + Computer Vision application

Practical use of YOLOv8

End-to-end system design (AI + Web)

Scalable solution for smart governance

📬 Author
Rohit Mane
AI | Computer Vision | Full Stack
