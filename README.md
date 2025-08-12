# todolist

This repository contains a simple webcam-based drawing application.

## Requirements
- Python 3
- OpenCV (`opencv-python`)
- MediaPipe
- NumPy

## Running
Install dependencies:
```
pip install opencv-python mediapipe numpy
```
Run the app:
```
python hand_paint.py
```
Controls:
- Move your index finger to draw on the screen.
- Press `c` to clear the canvas.
- Press `q` to quit.

## Build for Windows
To create a standalone executable on Windows, install PyInstaller and build:
```
pip install pyinstaller
pyinstaller --onefile hand_paint.py
```
The resulting `hand_paint.exe` will be located in the `dist` folder.

