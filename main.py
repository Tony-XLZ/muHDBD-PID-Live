import colorsys
import os
import sys
import time

from PyQt5.QtCore import QTimer
from PyQt5.QtGui import QIcon, QImage, QPixmap
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox
import pandas as pd
import matplotlib.pyplot as plt

import GUI
import cv2


class YLVP(QMainWindow, GUI.Ui_MainWindow):
    def __init__(self, parent=None):
        super(YLVP, self).__init__(parent)
        self.setupUi(self)
        self.initUI()

    def initUI(self):
        # Initialization
        QApplication.setStyle('Fusion')
        self.buttonChoose.clicked.connect(self.choose_camera)  # Button to switch camera
        self.ButtonStop.clicked.connect(self.toggle_pause)  # Button to pause
        self.buttoncamera.clicked.connect(self.save_picture)  # Button to capture picture
        self.buttonvideo.clicked.connect(self.save_video)  # Button to record video

        # Initialize camera
        self.cameraID = 0
        self.camera = cv2.VideoCapture(self.cameraID)
        if self.camera.isOpened():
            self.init_property()  # Camera initialization

            # Define paths for captures and videos
            results_dir = os.path.join(os.getcwd(), 'Results')
            self.captures_dir = os.path.join(results_dir, 'Captures')
            self.videos_dir = os.path.join(results_dir, 'Videos')

            # Create directories if they don't exist
            os.makedirs(self.captures_dir, exist_ok=True)
            os.makedirs(self.videos_dir, exist_ok=True)

            # Timers for live camera and video recording
            self.timer = QTimer(self)
            self.timer.timeout.connect(self.update_camera_frame)
            self.timer.start(15)

            self.timerVideo = QTimer(self)
            self.timerVideo.timeout.connect(self.record_video_frame)
        else:
            QMessageBox.critical(self, "Error", "Camera connection failed", QMessageBox.Ok)
            sys.exit()

    def update_camera_frame(self):
        # Update live camera feed
        ret, self.frame = self.camera.read()
        if ret:
            image_rgb = cv2.cvtColor(self.frame, cv2.COLOR_BGR2RGB)
            image_gray = cv2.cvtColor(self.frame, cv2.COLOR_BGR2GRAY)
            q_image = QImage(image_rgb.data, image_rgb.shape[1], image_rgb.shape[0], QImage.Format_RGB888)
            self.imagelabel.setPixmap(QPixmap.fromImage(q_image))
            hist = cv2.calcHist([image_gray], [0], None, [256], [0, 256])
            self.histWidget.histMP.plot(hist)

    def init_property(self):
        # Camera properties initialization
        self.FPS = 15
        self.property_values = {
            'brightness': self.camera.get(cv2.CAP_PROP_BRIGHTNESS),
            'contrast': self.camera.get(cv2.CAP_PROP_CONTRAST),
            'saturation': self.camera.get(cv2.CAP_PROP_SATURATION),
            'hue': self.camera.get(cv2.CAP_PROP_HUE),
            'sharpness': self.camera.get(cv2.CAP_PROP_SHARPNESS),
            'gamma': self.camera.get(cv2.CAP_PROP_GAMMA),
            'gain': self.camera.get(cv2.CAP_PROP_GAIN)
        }
        self.width = int(self.camera.get(cv2.CAP_PROP_FRAME_WIDTH))
        self.height = int(self.camera.get(cv2.CAP_PROP_FRAME_HEIGHT))
        self.size = (self.width, self.height)

    def choose_camera(self):
        # Switch between available cameras
        original_camera_id = self.cameraID
        for i in range(5):
            self.cameraID = (self.cameraID + 1) % 5
            self.camera.release()  # Release the previous camera
            try:
                self.camera = cv2.VideoCapture(self.cameraID)
                if self.camera.isOpened():
                    self.init_property()
                    self.status.showMessage("Camera switched", 3000)
                    return
                else:
                    self.camera.release()
            except Exception as e:
                print(f"Failed to open camera {self.cameraID}: {e}")
                continue
        # If no other camera is found, revert to the original camera ID
        self.cameraID = original_camera_id
        self.camera = cv2.VideoCapture(self.cameraID)
        if not self.camera.isOpened():
            QMessageBox.information(self, "Camera Switch", "No additional camera found", QMessageBox.Ok)
            self.status.showMessage("No additional camera found", 3000)
        else:
            self.init_property()
            self.status.showMessage("Switched back to original camera", 3000)

    def toggle_pause(self):
        # Pause or resume the camera feed
        if self.ButtonStop.isChecked():
            self.ButtonStop.setText("Continue")
            self.timer.stop()
            if self.buttonvideo.isChecked():
                self.timerVideo.stop()
            self.buttonvideo.setEnabled(False)
            self.status.showMessage("Paused")
        else:
            self.ButtonStop.setText("Pause")
            self.timer.start(30)
            if self.buttonvideo.isChecked():
                self.timerVideo.start(20)
                self.status.showMessage("Recording...")
            else:
                self.buttonvideo.setEnabled(True)
                self.status.showMessage("Continuing", 3000)

    def save_picture(self):
        # Capture and save a picture
        file_name_picture = os.path.join(self.captures_dir, f"PHOTO_{time.strftime('%Y%m%d%H%M%S')}.jpg")
        if self.ButtonStop.isChecked():
            cv2.imwrite(file_name_picture, self.frame)
        else:
            self.timer.stop()
            cv2.imwrite(file_name_picture, self.frame)
            self.imagelabel.setPixmap(QPixmap("image/black.png"))
            time.sleep(0.1)
            self.timer.start(20)
        self.status.showMessage(f"Picture successfully saved to {self.captures_dir}", 3000)

    def save_video(self):
        # Start or stop video recording
        if self.buttonvideo.isChecked():
            self.fourcc = cv2.VideoWriter_fourcc(*'MJPG')
            timestamp = time.strftime('%Y%m%d%H%M%S')
            video_folder = os.path.join(self.videos_dir, f"VIDEO_{timestamp}")
            os.makedirs(video_folder, exist_ok=True)
            self.plot_loc = os.path.join(video_folder, 'plot')
            self.csv_loc = os.path.join(video_folder, 'csv')
            os.makedirs(self.plot_loc, exist_ok=True)
            os.makedirs(self.csv_loc, exist_ok=True)
            file_name_video = os.path.join(video_folder, f"VIDEO_{timestamp}.avi")

            self.R, self.G, self.B, self.Y, self.L, self.V = [], [], [], [], [], []
            self.out = cv2.VideoWriter(file_name_video, self.fourcc, self.FPS, self.size)
            self.timerVideo.start(20)
            self.buttonvideo.setText("Stop")
            self.status.showMessage("Recording...")
        else:
            self.stop_video_recording()

    def stop_video_recording(self):
        # Stop video recording and save data
        self.timerVideo.stop()
        self.out.release()
        self.buttonvideo.setText("Record")
        self.status.showMessage(f"Video successfully saved to {self.videos_dir}", 3000)

        df = pd.DataFrame({'R': self.R, 'G': self.G, 'B': self.B, 'Y': self.Y, 'L': self.L, 'V': self.V})
        df['time'] = (df.index + 1) / self.FPS
        df.set_index('time', inplace=True)
        plt.plot(df['Y'], label='Y')
        plt.plot(df['L'], label='L')
        plt.plot(df['V'], label='V')
        plt.title("Brightness Plot")
        plt.xlabel("Time (seconds)")
        plt.ylabel("Brightness Value")
        plt.legend()
        plt.savefig(os.path.join(self.plot_loc, 'Brightness_plot.jpg'))
        plt.close()
        df.to_csv(os.path.join(self.csv_loc, 'RGBYLV_data.csv'))

    def record_video_frame(self):
        # Record video frames
        ret, frame = self.camera.read()
        if ret:
            self.out.write(frame)
            self.B.append(frame[:, :, 0].mean())
            self.G.append(frame[:, :, 1].mean())
            self.R.append(frame[:, :, 2].mean())
            self.Y.append(0.299 * self.R[-1] + 0.587 * self.G[-1] + 0.114 * self.B[-1])
            self.L.append(colorsys.rgb_to_hls(self.R[-1] / 255, self.G[-1] / 255, self.B[-1] / 255)[1] * 255)
            self.V.append(colorsys.rgb_to_hsv(self.R[-1] / 255, self.G[-1] / 255, self.B[-1] / 255)[2] * 255)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    mainUI = YLVP()
    mainUI.show()
    sys.exit(app.exec_())
