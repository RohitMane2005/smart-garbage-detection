# Detect only real garbage-like objects with confidence & size filtering

GARBAGE_CLASSES = {
    "bottle", "cup", "banana", "apple",
    "sandwich", "orange", "bag"
}

GARBAGE_CONF_THRESH = 0.45      # higher = fewer false positives
MIN_GARBAGE_AREA = 400          # ignore tiny detections


def detect_garbage(results):
    garbage_boxes = []

    for box in results.boxes:
        cls_id = int(box.cls[0])
        cls_name = results.names[cls_id]
        conf = float(box.conf[0])

        if cls_name not in GARBAGE_CLASSES:
            continue
        if conf < GARBAGE_CONF_THRESH:
            continue

        x1, y1, x2, y2 = box.xyxy[0]
        area = (x2 - x1) * (y2 - y1)

        if area < MIN_GARBAGE_AREA:
            continue

        garbage_boxes.append(box.xyxy[0])

    return garbage_boxes
