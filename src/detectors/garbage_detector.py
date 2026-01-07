GARBAGE_CLASSES = {
    "bottle", "cup", "banana", "apple",
    "sandwich", "orange", "bag"
}

def detect_garbage(results):
    garbage_boxes = []
    for r in results:
        for box in r.boxes:
            cls_name = r.names[int(box.cls)]
            if cls_name in GARBAGE_CLASSES:
                garbage_boxes.append(box)
    return garbage_boxes
