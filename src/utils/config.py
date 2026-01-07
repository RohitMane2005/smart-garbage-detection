import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

MODEL_PATH = os.path.join(BASE_DIR, "models", "yolov8n.pt")
VIDEO_PATH = os.path.join(BASE_DIR, "input_videos", "sample_video.mp4")
EVENT_DIR = os.path.join(BASE_DIR, "output_events", "images")
CONF_THRESHOLD = 0.4

# Garbage-related COCO classes
GARBAGE_CLASSES = {
    "bottle",
    "cup",
    "can",
    "plastic",
    "paper",
    "trash",
    "cell phone"
}
