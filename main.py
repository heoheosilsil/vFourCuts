import cv2
import numpy as np
import time
import mediapipe as mp
from tensorflow.keras.models import load_model


def count_peace_hands(frame, width, height):
    framergb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    # Get hand landmark prediction
    result = hands.process(framergb)

    count = 0

    # Post process the result
    if result.multi_hand_landmarks:
        for handslms in result.multi_hand_landmarks:
            landmarks = []
            for lm in handslms.landmark:
                # print(id, lm)
                lmx = int(lm.x * width)
                lmy = int(lm.y * height)

                landmarks.append([lmx, lmy])

            # Drawing landmarks on frames
            mpDraw.draw_landmarks(frame, handslms, mpHands.HAND_CONNECTIONS)

            # Predict gesture in Hand Gesture Recognition project
            prediction = model.predict([landmarks])
            print(prediction)
            classID = np.argmax(prediction)
            className = classNames[classID]

            if className == "peace":
                count += 1

    return count


# initialize mediapipe
mpHands = mp.solutions.hands
hands = mpHands.Hands(max_num_hands=5, min_detection_confidence=0.7)
mpDraw = mp.solutions.drawing_utils

# Load the gesture recognizer model
model = load_model('mp_hand_gesture')

# Load class names
f = open('gesture.names', 'r')
classNames = f.read().split('\n')
f.close()
print(classNames)

# Create a camera capture object
cap = cv2.VideoCapture(0)

# countdown time
countdown_time = 5

# number of repetitions
num_repeats = 4

# Size and initialization of image files to be saved
image_height, image_width = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT)), int(
    cap.get(cv2.CAP_PROP_FRAME_WIDTH))  # Adjust to the actual image size used
combined_image = np.zeros((2 * image_height, 2 * image_width, 3), dtype=np.uint8)

countdown = False

for row in range(2):
    for col in range(2):
        countdown_start_time = time.time()
        countdown_remaining_time = countdown_time  # Add initialization

        while True:
            ret, frame_original = cap.read()

            frame_display = frame_original.copy()

            num_hands = count_peace_hands(frame_display, image_width, image_height)

            # Countdown for 5 seconds when hand is detected
            if num_hands >= 1:
                countdown = True

            if countdown:
                countdown_elapsed_time = time.time() - countdown_start_time
                countdown_remaining_time = max(0, countdown_time - int(countdown_elapsed_time))

                if countdown_remaining_time == 0:
                    # Combine images after counting down for 5 seconds
                    combined_image[row * image_height:(row + 1) * image_height,
                    col * image_width:(col + 1) * image_width] = frame_original
                    print('Photo taken!')
                    countdown = False
                    break

            # display text
            cv2.putText(frame_display, f'Countdown: {countdown_remaining_time} seconds', (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1,
                        (0, 0, 255), 2)
            cv2.putText(frame_display, f'Hand: {num_hands}', (10, 70), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

            cv2.imshow('Finger Detection', frame_display)

            key = cv2.waitKey(1)
            if key & 0xFF == ord('q'):
                break

# Save image (excluding text)
cv2.imwrite('result_vfourcuts.png', combined_image)

# clear
cap.release()
cv2.destroyAllWindows()
