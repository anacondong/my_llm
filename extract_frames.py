import cv2
import os

# === CONFIG ===
video_path = "your_video.mp4"       # <- Change this to your actual video file
output_folder = "frames"            # <- Output folder to save frames
frame_interval = 300                 # <- Save 1 frame every N frames

# === SETUP ===
os.makedirs(output_folder, exist_ok=True)

cap = cv2.VideoCapture(video_path)
if not cap.isOpened():
    print("Error: Cannot open video.")
    exit()

frame_count = 0
saved_count = 0

while True:
    ret, frame = cap.read()
    if not ret:
        break

    if frame_count % frame_interval == 0:
        filename = os.path.join(output_folder, f"frame_{saved_count:04d}.jpg")
        cv2.imwrite(filename, frame)
        print(f"Saved {filename}")
        saved_count += 1

    frame_count += 1

cap.release()
print(f"✅ Done! Extracted {saved_count} frames to '{output_folder}'")
