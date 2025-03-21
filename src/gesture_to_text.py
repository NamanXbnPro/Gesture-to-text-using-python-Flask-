import cv2
import mediapipe as mp
import numpy as np

# Initialize Mediapipe Hands
mp_hands = mp.solutions.hands
hands = mp_hands.Hands(max_num_hands=1, min_detection_confidence=0.7)
mp_drawing = mp.solutions.drawing_utils

# Function to recognize gestures
def recognize_gesture(landmarks):
    # Get landmark positions
    thumb_tip = landmarks[mp_hands.HandLandmark.THUMB_TIP]
    thumb_ip = landmarks[mp_hands.HandLandmark.THUMB_IP]

    index_tip = landmarks[mp_hands.HandLandmark.INDEX_FINGER_TIP]
    index_pip = landmarks[mp_hands.HandLandmark.INDEX_FINGER_PIP]

    middle_tip = landmarks[mp_hands.HandLandmark.MIDDLE_FINGER_TIP]
    middle_pip = landmarks[mp_hands.HandLandmark.MIDDLE_FINGER_PIP]

    ring_tip = landmarks[mp_hands.HandLandmark.RING_FINGER_TIP]
    ring_pip = landmarks[mp_hands.HandLandmark.RING_FINGER_PIP]

    pinky_tip = landmarks[mp_hands.HandLandmark.PINKY_TIP]
    pinky_pip = landmarks[mp_hands.HandLandmark.PINKY_PIP]

    # Thumbs Up: Thumb is extended, other fingers are closed
    if (thumb_tip.y < thumb_ip.y and
        index_tip.y > index_pip.y and
        middle_tip.y > middle_pip.y and
        ring_tip.y > ring_pip.y and
        pinky_tip.y > pinky_pip.y):
        return "Thumbs Up: Good Job!"

    # Peace Sign: Index and Middle fingers are extended, others are closed
    if (index_tip.y < index_pip.y and
        middle_tip.y < middle_pip.y and
        ring_tip.y > ring_pip.y and
        pinky_tip.y > pinky_pip.y):
        return "Peace Sign: Peace!"

    # Fist: All fingers are closed
    if (index_tip.y > index_pip.y and
        middle_tip.y > middle_pip.y and
        ring_tip.y > ring_pip.y and
        pinky_tip.y > pinky_pip.y):
        return "Fist: Stop!"

    # Open Hand: All fingers are extended
    if (index_tip.y < index_pip.y and
        middle_tip.y < middle_pip.y and
        ring_tip.y < ring_pip.y and
        pinky_tip.y < pinky_pip.y):
        return "Open Hand: Hello!"

    # OK Sign: Thumb and index finger tips are close, forming a circle
    if (abs(thumb_tip.x - index_tip.x) < 0.05 and
        abs(thumb_tip.y - index_tip.y) < 0.05 and
        middle_tip.y > middle_pip.y and
        ring_tip.y > ring_pip.y and
        pinky_tip.y > pinky_pip.y):
        return "OK Sign: Okay!"

    # Swag Sign: Thumb and pinky finger are extended, others are closed
    if (thumb_tip.y < thumb_ip.y and
        pinky_tip.y < pinky_pip.y and
        index_tip.y > index_pip.y and
        middle_tip.y > middle_pip.y and
        ring_tip.y > ring_pip.y):
        return "Swag Sign: Swag!"

    # Heart Sign: Index and middle fingers are bent to form a heart shape
    if (index_tip.y > index_pip.y and
        middle_tip.y > middle_pip.y and
        abs(index_tip.x - middle_tip.x) < 0.05 and
        ring_tip.y > ring_pip.y and
        pinky_tip.y > pinky_pip.y):
        return "Heart Sign: Love!"

    # Default: Unknown gesture
    return "Unknown Gesture"

# Capture video from webcam
cap = cv2.VideoCapture(0)

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    # Flip the image horizontally for a later selfie-view display
    frame = cv2.flip(frame, 1)

    # Convert the BGR image to RGB
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    # Process the image and detect hands
    results = hands.process(rgb_frame)

    # Draw hand landmarks and recognize gestures
    if results.multi_hand_landmarks:
        for hand_landmarks in results.multi_hand_landmarks:
            mp_drawing.draw_landmarks(frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)
            gesture = recognize_gesture(hand_landmarks.landmark)

            # Display the recognized gesture text
            cv2.putText(frame, gesture, (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2, cv2.LINE_AA)

    # Display the frame
    cv2.imshow('Hand Gesture Recognition', frame)

    # Break the loop on 'q' key press
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the capture and close windows
cap.release()
cv2.destroyAllWindows()
