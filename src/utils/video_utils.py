import cv2

def open_video(path):
    return cv2.VideoCapture(path)

def read_frame(cap):
    return cap.read()

def close_video(cap):
    cap.release()
