# VFourCuts(브이네컷)

## Overview

**VFourCuts** is a photo booth application written in Python that performs real-time gesture recognition and automatically captures photos when a V-sign is detected. This program uses OpenCV and Tensorflow for gesture recognition and captures and composes images after a countdown.

## Key Points:

### 1. Hand Gesture Recognition:

- The script uses the MediaPipe library for hand landmark prediction and recognizes the V-sign(peace) gesture in real-time camera frames.

### 2. Gesture Prediction Model:

- A pre-trained TensorFlow/Keras model for hand gesture recognition is loaded using `load_model`. The model is designed to predict gestures based on hand landmarks.

### 3. Camera Capture and Countdown:

- The script captures video frames from the default camera (`cv2.VideoCapture(0)`).
- A countdown is initiated when the V-sign(peace) gesture is detected, and images are captured every 5 seconds for a total of 4 repetitions.

### 4. Image Processing:

- Hand landmarks are extracted, and the V-sign(peace) gesture is predicted for each detected hand.
- Landmarks are visualized on the frames using `mpDraw.draw_landmarks`.
- Images are combined into a single image after a 5-second countdown.

## Installation

**Supported Python version:** `3.11`

1. Install Python: Download and install Python from the [official Python website](https://www.python.org/downloads/) Make sure you are using a supported version of Python.
2. Download the sources: Run `git clone https://github.com/heoheosilsil/vFourCuts.git` or [download the zip archive](https://codeload.github.com/heoheosilsil/vFourCuts/zip/refs/heads/main) of this project.
3. Install the dependencies: In the project directory, use the command `pip install -r requirements.txt` to install the dependencies.

## Usage

1. Run the `main.py` file.
2. Once the program starts, gesture detection will start.
3. When a V-Sign is detected, a 5 second countdown will start and a photo will be taken.
4. A total of 4 photos will be composited and saved in a file named `result_vfourcuts.png`.

## Screenshot

When the program is running, you will see:

- A countdown timer
- The current number of detected V-Signs

## Result

![Result image](result_vfourcuts.png)

## Dependencies

The project uses OpenCV for image processing and Tensorflow for gesture recognition. A detailed list of dependencies and their versions can be found [here](requirements.txt).

## References

This program uses pre-trained datasets from the following website for machine learning gesture recognition.

- https://techvidvan.com/tutorials/hand-gesture-recognition-tensorflow-opencv/

## Limitations:

- The technique requires nearly perfect top-down views for accurate gesture recognition.

## Contributions

If you would like to contribute to this project, please open a pull request or issue. All contributions are welcome!
