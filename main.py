import cv2
import numpy as np
import time


def detect_fingers(frame):
    lower_skin = np.array([0, 20, 70], dtype=np.uint8)
    upper_skin = np.array([20, 255, 255], dtype=np.uint8)

    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    mask = cv2.inRange(hsv, lower_skin, upper_skin)

    # noise removal
    kernel = np.ones((5, 5), np.uint8)
    mask = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel)

    contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    fingers = 0

    for contour in contours:
        area = cv2.contourArea(contour)

        # Exclude objects that are too small or too large
        epsilon = 0.02 * cv2.arcLength(contour, True)
        approx = cv2.approxPolyDP(contour, epsilon, True)

        if len(approx) == 3:
            fingers += 1

    return fingers


# Create a camera capture object
cap = cv2.VideoCapture(0)

# countdown time
countdown_time = 5

# number of repetitions
num_repeats = 4

# Size and initialization of image files to be saved
image_height, image_width = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT)), int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))  # Adjust to the actual image size used
combined_image = np.zeros((2 * image_height, 2 * image_width, 3), dtype=np.uint8)

for row in range(2):
    for col in range(2):
        countdown_start_time = time.time()
        countdown_remaining_time = countdown_time  # Add initialization

        while True:
            ret, frame = cap.read()

            num_fingers = detect_fingers(frame)

            # Countdown for 5 seconds when 2 finger is detected
            if num_fingers == 2:
                countdown_elapsed_time = time.time() - countdown_start_time
                countdown_remaining_time = max(0, countdown_time - int(countdown_elapsed_time))

                if countdown_remaining_time == 0:
                    # Combine images after counting down for 5 seconds
                    combined_image[row * image_height:(row + 1) * image_height, col * image_width:(col + 1) * image_width] = frame
                    print('Photo taken!')
                    break

            # display text
            cv2.putText(frame, f'Countdown: {countdown_remaining_time} seconds', (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)
            cv2.putText(frame, f'Fingers: {num_fingers}', (10, 70), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

            cv2.imshow('Finger Detection', frame)

            key = cv2.waitKey(1)
            if key & 0xFF == ord('q'):
                break

# Save image (excluding text)
cv2.imwrite('result_vfourcuts.png', combined_image)

# clear
cap.release()
cv2.destroyAllWindows()
