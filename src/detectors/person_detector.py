def detect_persons(results, model, conf_thresh):
    persons = []

    for box in results.boxes:
        cls_id = int(box.cls[0])
        label = model.names[cls_id]
        conf = float(box.conf[0])

        if label == "person" and conf >= conf_thresh:
            persons.append(box.xyxy[0])

    return persons
