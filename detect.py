from ultralytics import YOLO
import cv2
import os
import sys

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

model = YOLO("yolov8n.pt")

video_path = sys.argv[1]

cap = cv2.VideoCapture(video_path)

if not cap.isOpened():
    print("Cannot open video:", video_path)
    exit()

width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
fps = cap.get(cv2.CAP_PROP_FPS)

if fps == 0:
    fps = 30

output_dir = os.path.join(BASE_DIR, "static", "output")
os.makedirs(output_dir, exist_ok=True)

output_path = os.path.join(output_dir, "output.mp4")

print("Saving to:", output_path)

fourcc = cv2.VideoWriter_fourcc(*"mp4v")
out = cv2.VideoWriter(output_path, fourcc, fps, (width, height))

while True:

    ret, frame = cap.read()

    if not ret:
        break

    results = model(frame)

    annotated = results[0].plot()

    out.write(annotated)

cap.release()
out.release()

print("Detection Completed Successfully!")
print("Saved:", output_path)