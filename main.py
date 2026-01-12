import cv2
import numpy as np
import mediapipe as mp
from mediapipe.tasks import python
from mediapipe.tasks.python import vision


def draw_landmarks_on_image(rgb_image, detection_result):
    annotated_image = np.copy(rgb_image)

    height, width, _ = annotated_image.shape

    for hand_landmarks in detection_result.hand_landmarks:
        for landmark in hand_landmarks:
            x = int(landmark.x * width)
            y = int(landmark.y * height)

            cv2.circle(
                annotated_image,
                (x, y),
                radius=4,
                color=(0, 255, 0),
                thickness=-1
            )

    return annotated_image


# -------------------------
# Load MediaPipe hand model
# -------------------------
base_options = python.BaseOptions(
    model_asset_path="hand_landmarker.task"
)

options = vision.HandLandmarkerOptions(
    base_options=base_options,
    num_hands=2
)

detector = vision.HandLandmarker.create_from_options(options)

# -------------------------
# Load image
# -------------------------
image = mp.Image.create_from_file("image.jpg")

# -------------------------
# Run detection
# -------------------------
detection_result = detector.detect(image)

# -------------------------
# Draw & display result
# -------------------------
annotated_image = draw_landmarks_on_image(
    image.numpy_view(),
    detection_result
)

annotated_image_bgr = cv2.cvtColor(
    annotated_image,
    cv2.COLOR_RGB2BGR
)

# Resize image to make popup smaller
scale = 0.4 # adjust this number if needed
small_image = cv2.resize(
    annotated_image_bgr,
    None,
    fx=scale,
    fy=scale,
    interpolation=cv2.INTER_AREA
)

cv2.imshow("Hand Landmarks", small_image)
cv2.waitKey(0)
cv2.destroyAllWindows()