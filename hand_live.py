import cv2
import numpy as np
import mediapipe as mp
from mediapipe.tasks import python
from mediapipe.tasks.python import vision

# -------------------------
# DRAW HAND LANDMARKS
# -------------------------
def draw_landmarks_on_image(rgb_image, detection_result):
    annotated_image = np.copy(rgb_image)
    h, w, _ = annotated_image.shape

    for i, hand_landmarks in enumerate(detection_result.hand_landmarks):
        for lm in hand_landmarks:
            x, y = int(lm.x * w), int(lm.y * h)
            cv2.circle(annotated_image, (x, y), 4, (0, 255, 0), -1)

        connections = [
            (0,1),(1,2),(2,3),(3,4),
            (0,5),(5,6),(6,7),(7,8),
            (0,9),(9,10),(10,11),(11,12),
            (0,13),(13,14),(14,15),(15,16),
            (0,17),(17,18),(18,19),(19,20)
        ]
        for start, end in connections:
            x1, y1 = int(hand_landmarks[start].x * w), int(hand_landmarks[start].y * h)
            x2, y2 = int(hand_landmarks[end].x * w), int(hand_landmarks[end].y * h)
            cv2.line(annotated_image, (x1, y1), (x2, y2), (0, 255, 0), 2)

        if detection_result.handedness and len(detection_result.handedness[i]) > 0:
            handedness = detection_result.handedness[i][0].category_name
        else:
            handedness = "Unknown"

        wrist_x = int(hand_landmarks[0].x * w)
        wrist_y = int(hand_landmarks[0].y * h) - 10
        cv2.putText(annotated_image, handedness, (wrist_x, wrist_y),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255), 2)

    return annotated_image

# -------------------------
# HAND LANDMARKER SETUP
# -------------------------
base_options = python.BaseOptions(model_asset_path="hand_landmarker.task")
options = vision.HandLandmarkerOptions(
    base_options=base_options,
    running_mode=vision.RunningMode.VIDEO,  # VIDEO mode for main-thread processing
    num_hands=2
)
landmarker = vision.HandLandmarker.create_from_options(options)

# -------------------------
# WEBCAM CAPTURE
# -------------------------
cap = cv2.VideoCapture(0)
if not cap.isOpened():
    print("Error: Cannot open webcam.")
    exit()

try:
    while True:
        ret, frame = cap.read()
        if not ret:
            break

        # Convert BGR → RGB
        rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        mp_image = mp.Image(image_format=mp.ImageFormat.SRGB, data=rgb)

        # Detect hands
        timestamp_ms = int(cv2.getTickCount() / cv2.getTickFrequency() * 1000)
        detection_result = landmarker.detect_for_video(mp_image, timestamp_ms)

        # Draw landmarks
        annotated = draw_landmarks_on_image(rgb, detection_result)
        annotated_bgr = cv2.cvtColor(annotated, cv2.COLOR_RGB2BGR)

        # Resize smaller for display
        scaled = cv2.resize(annotated_bgr, None, fx=0.5, fy=0.5)
        cv2.imshow("Live Hand Landmarks", scaled)

        if cv2.waitKey(1) & 0xFF == 27:  # ESC to exit
            break

finally:
    cap.release()
    cv2.destroyAllWindows()
    landmarker.close()
