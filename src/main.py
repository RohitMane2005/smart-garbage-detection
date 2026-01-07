import cv2
import sys
from ultralytics import YOLO

from utils.config import VIDEO_PATH, MODEL_PATH, EVENT_DIR, CONF_THRESHOLD
from utils.video_utils import open_video, read_frame, close_video
from utils.image_utils import save_full_frame

from detectors.person_detector import detect_persons
from detectors.garbage_detector import detect_garbage
from detectors.littering_detector import LitteringDetector


def main(video_path):
    print("[INFO] Loading YOLO model...")
    model = YOLO(MODEL_PATH)

    littering_detector = LitteringDetector()

    print("[INFO] Opening video...")
    cap = open_video(video_path)

    if not cap.isOpened():
        print(f"[ERROR] Cannot open video: {video_path}")
        sys.exit(1)

    while True:
        ret, frame = read_frame(cap)
        if not ret:
            break

        results = model(frame, verbose=False)[0]

        persons = detect_persons(results, model, CONF_THRESHOLD)
        garbage = detect_garbage(results)

        if littering_detector.is_littering(persons, garbage):
            path = save_full_frame(frame, EVENT_DIR)
            print(f"[EVENT] Person threw garbage → saved: {path}")

        annotated_frame = frame.copy()

        # Draw PERSON boxes (green)
        for p in persons:
            x1, y1, x2, y2 = map(int, p)
            cv2.rectangle(annotated_frame, (x1, y1), (x2, y2), (0, 255, 0), 2)
            cv2.putText(
                annotated_frame,
                "Person",
                (x1, y1 - 10),
                cv2.FONT_HERSHEY_SIMPLEX,
                0.6,
                (0, 255, 0),
                2
            )

        # Draw GARBAGE boxes (red)
        for g in garbage:
            gx1, gy1, gx2, gy2 = map(int, g.xyxy[0])
            cls_name = results.names[int(g.cls[0])]

            cv2.rectangle(annotated_frame, (gx1, gy1), (gx2, gy2), (0, 0, 255), 2)
            cv2.putText(
                annotated_frame,
                f"Garbage: {cls_name}",
                (gx1, gy1 - 10),
                cv2.FONT_HERSHEY_SIMPLEX,
                0.6,
                (0, 0, 255),
                2
            )

        cv2.imshow("Smart Garbage Detection", annotated_frame)

        if cv2.waitKey(1) & 0xFF == ord("q"):
            break

    close_video(cap)
    cv2.destroyAllWindows()
    print("[INFO] System stopped")


if __name__ == "__main__":
    # Use uploaded video if provided, else fallback
    video_path = sys.argv[1] if len(sys.argv) > 1 else VIDEO_PATH
    main(video_path)
