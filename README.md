# Object Size Estimation with Hand Gesture Recognition using OpenCV

This Python script utilizes OpenCV for hand gesture recognition, specifically detecting the "peace" gesture, and estimates the size of the recognized hands based on a reference object. The project is inspired by Adrian Rosebrock's tutorials on PyImageSearch.

## Key Points:
### 1. Hand Gesture Recognition:
   - The script uses the MediaPipe library for hand landmark prediction and recognizes the "peace" gesture in real-time camera frames.

### 2. Gesture Prediction Model:
   - A pre-trained TensorFlow/Keras model for hand gesture recognition is loaded using `load_model`. The model is designed to predict gestures based on hand landmarks.

### 3. Camera Capture and Countdown:
   - The script captures video frames from the default camera (`cv2.VideoCapture(0)`).
   - A countdown is initiated when the "peace" gesture is detected, and images are captured every 5 seconds for a total of 4 repetitions.

### 4. Image Processing:
   - Hand landmarks are extracted, and the "peace" gesture is predicted for each detected hand.
   - Landmarks are visualized on the frames using `mpDraw.draw_landmarks`.
   - Images are combined into a single image after a 5-second countdown.

### 5. Result and Cleanup:
   - The combined image, excluding text, is saved as 'result_vfourcuts.png'.
   - The script releases the camera and closes OpenCV windows.

Requirements:
Install Python: Download and install Python from the official Python website.
Install OpenCV: In your Python environment, run pip install opencv-python to install OpenCV.

## How to Run:

Download the vFourCuts.py file and run it in your Python environment.
Upon starting the program, webcam-based finger detection will commence.
When 2 fingers are detected, a 5-second countdown initiates, and upon completion, a photo is captured.
A total of 4 photos are composited and saved as result_vfourcuts.png.

## Example and Results:

When the program is running, you will see:

- A countdown timer
- The current number of fingers detected

The captured image will be saved in a file named `result_vfourcuts.png`.

## Limitations:
- The technique requires nearly perfect top-down views for accurate size calculations.
- Images may be prone to radial and tangential lens distortion, leading to uneven object dimensions.

## Contributing

If you would like to contribute to this project, please send a pull request or open an issue. All contributions are welcome!