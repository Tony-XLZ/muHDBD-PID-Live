# μHD-PID Live

μHD-PID Live is a PyQt5-based application designed to capture and record live video feeds from system cameras, while performing real-time analysis on the visual data. It includes a graphical user interface that displays both the live video feed and a histogram representing the pixel intensity distribution, enabling insightful analysis of captured frames.

## Features
- **Live Camera Feed**: View real-time camera feed with an option to switch between multiple connected cameras.
- **Real-Time Histogram**: Displays a histogram of pixel intensity values for the current frame in real time.
- **Image Capture**: Capture and save individual frames as JPEG images.
- **Video Recording**: Record live video, along with logging RGB and brightness data.
- **Brightness Analysis**: Generate and save brightness plots and export the data as CSV files.

## Project Structure
The project consists of three main Python files:

1. **MatplotlibWidget.py**
   - Contains the `MyMplCanvas` class, which defines a custom Matplotlib canvas for displaying the histogram.
   - Includes the `MatplotlibWidget` class, which integrates the histogram into the main PyQt5 application.

2. **GUI.py**
   - Defines the main user interface (`Ui_MainWindow`) for the application, with sections for both the histogram and camera display.
   - Contains buttons for camera control (e.g., switching cameras, pausing the feed, recording, and capturing).

3. **main.py**
   - The main entry point for the application.
   - Contains the `YLVP` class that extends `QMainWindow` and provides the core functionality, such as camera setup, live video display, histogram updating, image capture, and video recording.
   - Initializes the PyQt5 event loop to run the application.

## Installation
To run μHD-PID Live, ensure you have the following dependencies installed:

- Python 3.8+
- PyQt5
- OpenCV (`cv2`)
- Matplotlib
- Pandas

You can install the dependencies using pip:

```sh
pip install -r requirements.txt
```

## Usage
1. Clone the repository or download the source code.
2. Navigate to the directory containing the source code.
3. Run the main application:

```sh
python main.py
```

## Directory Structure
- **Results/**: Directory where captured images and recorded videos are saved.
  - **Captures/**: Stores captured images.
  - **Videos/**: Stores recorded videos, along with associated brightness plots and CSV data files.

## System Requirements
- **Operating System**: Windows, macOS, or Linux
- **Python Version**: Python 3.8 or higher
- **Hardware**: A webcam or any compatible camera for capturing video

## Screenshot
![Application Screenshot](demo/screenshot.png)

## Author
Developed by Tony Wu.

## License
This project is licensed under the MIT License. See the `LICENSE` file for more details.

