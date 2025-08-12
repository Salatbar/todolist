import cv2
import mediapipe as mp
import numpy as np


def main():
    # Initialize webcam capture
    cap = cv2.VideoCapture(0)
    if not cap.isOpened():
        print("Error: Cannot open webcam")
        return

    # MediaPipe hands setup
    mp_hands = mp.solutions.hands
    hands = mp_hands.Hands(max_num_hands=1, min_detection_confidence=0.7)
    mp_drawing = mp.solutions.drawing_utils

    canvas = None

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        frame = cv2.flip(frame, 1)
        if canvas is None:
            canvas = np.zeros_like(frame)

        # Convert BGR to RGB for MediaPipe processing
        rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        result = hands.process(rgb_frame)

        if result.multi_hand_landmarks:
            for hand_landmarks in result.multi_hand_landmarks:
                h, w, _ = frame.shape
                index_finger_tip = hand_landmarks.landmark[8]
                x = int(index_finger_tip.x * w)
                y = int(index_finger_tip.y * h)

                cv2.circle(canvas, (x, y), 5, (0, 0, 255), -1)
                mp_drawing.draw_landmarks(frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)

        frame = cv2.add(frame, canvas)
        cv2.imshow('Hand Paint', frame)
        key = cv2.waitKey(1) & 0xFF
        if key == ord('c'):
            canvas = np.zeros_like(canvas)
        elif key == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()


if __name__ == "__main__":
    main()
