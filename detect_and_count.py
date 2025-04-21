import cv2
from ultralytics import YOLO

# Load your trained model
model = YOLO("runs/detect/train3/weights/best.pt")

# Open video file
video_path = "your_video.mp4"  # Replace this with your actual file
cap = cv2.VideoCapture(video_path)

# Initialize counter
basket_count = 0
frame_count = 0
ball_previous_in_hoop = False

# Define class names
class_names = ["basketball", "hoop"]

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    results = model(frame, verbose=False)[0]

    balls = []
    hoops = []

    for result in results.boxes.data.tolist():
        x1, y1, x2, y2, conf, cls = result
        cls = int(cls)
        if class_names[cls] == "basketball":
            balls.append(((x1 + x2) / 2, (y1 + y2) / 2))  # center of ball
            cv2.rectangle(frame, (int(x1), int(y1)), (int(x2), int(y2)), (0, 0, 255), 2)  # red box
        elif class_names[cls] == "hoop":
            hoops.append(((x1, y1), (x2, y2)))
            cv2.rectangle(frame, (int(x1), int(y1)), (int(x2), int(y2)), (0, 255, 0), 2)  # green box

    # Check if ball is inside any hoop
    ball_in_hoop = False
    for ball in balls:
        for (hx1, hy1), (hx2, hy2) in hoops:
            if hx1 < ball[0] < hx2 and hy1 < ball[1] < hy2:
                ball_in_hoop = True
                break

    # Count only when ball goes **into** hoop
    if ball_in_hoop and not ball_previous_in_hoop:
        basket_count += 1
    ball_previous_in_hoop = ball_in_hoop

    # Display the count
    cv2.putText(frame, f"Basket Count: {basket_count}", (20, 40),
                cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 0), 2)

    cv2.imshow("Detection", frame)
    if cv2.waitKey(1) == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
