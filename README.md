# vFourCuts

## Overview

`vFourCuts` is a Python program that performs real-time finger detection and automatically captures photos when a specific number of fingers are detected. This program uses OpenCV for finger detection and captures and composites images after a countdown for each detected number of fingers.

## Installation

To use this program, Python and OpenCV are required.

1. Install Python: Download and install Python from the [official Python website](https://www.python.org/downloads/).
2. Install OpenCV: In your Python environment, use the command `pip install opencv-python` to install OpenCV.

## Usage

1. Download the `vFourCuts.py` file and run it in your Python environment.
2. Once the program starts, finger detection will begin using the webcam.
3. When 2 fingers are detected, a 5-second countdown will start, and upon completion, a photo will be captured.
4. A total of 4 photos will be composited and saved in a file named `result_vfourcuts.png`.

## Example and Results

When the program is running, you will see:

- A countdown timer
- The current number of fingers detected

The captured image will be saved in a file named `result_vfourcuts.png`.

## Contributing

If you would like to contribute to this project, please send a pull request or open an issue. All contributions are welcome!
