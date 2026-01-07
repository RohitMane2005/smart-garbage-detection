import cv2
import os
from datetime import datetime

def save_full_frame(frame, save_dir):
    os.makedirs(save_dir, exist_ok=True)

    filename = f"littering_{datetime.now().strftime('%Y%m%d_%H%M%S_%f')}.jpg"
    path = os.path.join(save_dir, filename)

    cv2.imwrite(path, frame)
    return path
