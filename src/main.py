import cv2
import sys
from ultralytics import YOLO

from utils.config import VIDEO_PATH, MODEL_PATH, EVENT_DIR, CONF_THRESHOLD
from utils.video_utils import open_video, read_frame, close_video
from utils.image_utils import save_full_frame

from detectors.person_detector import detect_persons
from detectors.garbage_detector import detect_garbage
from detectors.littering_detector import LitteringDetector


SKIP_FRAMES = 5
RESIZE_DIM = (640, 360)


def main(video_path):
    print("[INFO] Loading YOLO model...")
    model = YOLO(MODEL_PATH)   # use yolov8n.pt for best speed

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

        results = model(frame, verbose=False)[0]

        persons = detect_persons(results, model, CONF_THRESHOLD)
        garbage = detect_garbage(results)

        if detector.is_littering(persons, garbage):
            path = save_full_frame(frame, EVENT_DIR)
            print(f"[EVENT] Littering detected → {path}")

        annotated = frame.copy()

        for p in persons:
            x1, y1, x2, y2 = map(int, p)
            cv2.rectangle(annotated, (x1,y1), (x2,y2), (0,255,0), 2)

        for g in garbage:
            gx1, gy1, gx2, gy2 = map(int, g)
            cv2.rectangle(annotated, (gx1,gy1), (gx2,gy2), (0,0,255), 2)

        cv2.imshow("Smart Garbage Detection", annotated)
        if cv2.waitKey(1) & 0xFF == ord("q"):
            break

    close_video(cap)
    cv2.destroyAllWindows()
    print("[INFO] Processing finished")


if __name__ == "__main__":
    video = sys.argv[1] if len(sys.argv) > 1 else VIDEO_PATH
    main(video)
