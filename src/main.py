import cv2
import sys
from ultralytics import YOLO

from utils.config import VIDEO_PATH, MODEL_PATH, EVENT_DIR, CONF_THRESHOLD
from utils.video_utils import open_video, read_frame, close_video
from utils.image_utils import save_full_frame

from detectors.person_detector import detect_persons
from detectors.garbage_detector import detect_garbage
from detectors.littering_detector import LitteringDetector


# ===== PERFORMANCE OPTIMIZATION FOR RENDER =====
SKIP_FRAMES = 8
RESIZE_DIM = (480, 270)


def main(video_path):
    print("[INFO] Loading YOLO model...")

    # Load YOLOv8 nano model (fastest)
    model = YOLO(MODEL_PATH)
    model.fuse()   # CPU optimization (VERY IMPORTANT for Render)

    detector = LitteringDetector()
    cap = open_video(video_path)

    frame_count = 0

    while True:
        ret, frame = read_frame(cap)
        if not ret:
            break

        frame_count += 1
        if frame_count % SKIP_FRAMES != 0:
            continue

        frame = cv2.resize(frame, RESIZE_DIM)

        # YOLO inference
        results = model(frame, verbose=False)[0]

        persons = detect_persons(results, model, CONF_THRESHOLD)
        garbage = detect_garbage(results)

        # Event detection
        if detector.is_littering(persons, garbage):
            path = save_full_frame(frame, EVENT_DIR)
            print(f"[EVENT] Littering detected → {path}")

    close_video(cap)
    print("[INFO] Processing finished")


if __name__ == "__main__":
    video = sys.argv[1] if len(sys.argv) > 1 else VIDEO_PATH
    main(video)
