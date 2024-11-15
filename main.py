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
        # initialisation
        QApplication.setStyle('Fusion')
        self.buttonChoose.clicked.connect(self.ChooseCamera)  # button-switch cam
        self.ButtonStop.clicked.connect(self.timeStop)  # button-pause
        self.buttoncamera.clicked.connect(self.SavePicture)  # button-capture
        self.buttonvideo.clicked.connect(self.SaveVideo)  # button-record

        # invoke camera
        self.cameraID = 0
        self.camera = cv2.VideoCapture(self.cameraID)
        if self.camera.isOpened():
            self.initProperty()  # camera init
            self.filenameImage = os.getcwd() + '\Results\Captures'
            self.filenameVideo = os.getcwd() + '\Results\Videos'
            self.timer = QTimer(self)  # init a timer
            self.timer.timeout.connect(self.CameraPicture)  # show real time data
            self.timer.start(15)
            self.timerVideo = QTimer(self)  # init the second timer
            self.timerVideo.timeout.connect(self.VideoFrame)  # loop the camera reading function
        else:
            reply = QMessageBox.critical(self, "error", "camera connection failed", QMessageBox.Ok)
            if reply == QMessageBox.Ok:
                sys.exit()

    def CameraPicture(self):
        # live camera function
        ret, self.frame = self.camera.read()  # get frame from camera
        self.image = cv2.cvtColor(self.frame, cv2.COLOR_BGR2RGB)
        self.image_gray = cv2.cvtColor(self.frame, cv2.COLOR_BGR2GRAY)
        Q_image = QImage(self.image.data, self.image.shape[1], self.image.shape[0], QImage.Format_RGB888)
        self.imagelabel.setPixmap(QPixmap.fromImage(Q_image))
        self.hist = cv2.calcHist([self.image_gray], [0], None, [256], [0, 256])  # calculate histogram
        self.histWidget.histMP.plot(self.hist)  # show histogram

    def initProperty(self):
        # camera init function
        self.FPS = 15  # default fps
        self.PropertyValue = {}
        self.PropertyValue['bright'] = self.camera.get(cv2.CAP_PROP_BRIGHTNESS)
        self.PropertyValue['contrast'] = self.camera.get(cv2.CAP_PROP_CONTRAST)
        self.PropertyValue['saturation'] = self.camera.get(cv2.CAP_PROP_SATURATION)
        self.PropertyValue['hue'] = self.camera.get(cv2.CAP_PROP_HUE)
        self.PropertyValue['sharpness'] = self.camera.get(cv2.CAP_PROP_SHARPNESS)
        self.PropertyValue['gamma'] = self.camera.get(cv2.CAP_PROP_GAMMA)
        self.PropertyValue['gain'] = self.camera.get(cv2.CAP_PROP_GAIN)
        self.width = self.camera.get(cv2.CAP_PROP_FRAME_WIDTH)
        self.height = self.camera.get(cv2.CAP_PROP_FRAME_HEIGHT)

        # save shortcut for later use
        self.brightDefault = self.PropertyValue['bright']
        self.contrastDefault = self.PropertyValue['contrast']
        self.saturationDefault = self.PropertyValue['saturation']
        self.hueDefault = self.PropertyValue['hue']
        self.sharpnessDefault = self.PropertyValue['sharpness']
        self.gammaDefault = self.PropertyValue['gamma']
        self.gainDefault = self.PropertyValue['gain']
        self.Size = (int(self.width), int(self.height))

    def ChooseCamera(self):
        # function for camera switch
        cameraIDD = self.cameraID
        for i in range(0, 8):
            self.cameraID = self.cameraID + 1
            if self.cameraID >= 5:
                self.cameraID = 0
            self.camera = cv2.VideoCapture(self.cameraID)
            if self.camera.isOpened():
                if self.cameraID == cameraIDD:
                    self.initProperty()
                    QMessageBox.information(self, "camera switch", "no camera found", QMessageBox.Ok, QMessageBox.Ok)
                    self.status.showMessage("no camera found", 3000)
                else:
                    self.initProperty()
                    self.status.showMessage("camera switched", 3000)
                break

    def timeStop(self):
        # button checking
        if self.ButtonStop.isChecked():
            self.ButtonStop.setText("continue")
            self.timer.stop()
            if self.buttonvideo.isChecked():
                self.timerVideo.stop()
            else:
                self.buttonvideo.setEnabled(False)
            self.status.showMessage("pause")
        else:
            self.ButtonStop.setText("pause")
            self.timer.start(30)
            if self.buttonvideo.isChecked():
                self.timerVideo.start(20)
                self.status.showMessage("recording……")
            else:
                self.buttonvideo.setEnabled(True)
                self.status.showMessage("continue", 3000)

    def SavePicture(self):
        # button-capture function
        fileNamePicture = self.filenameImage + "\PHOTO_" + time.strftime("%Y%m%d%H%M%S", time.localtime()) + ".jpg"
        if self.ButtonStop.isChecked():
            cv2.imencode('.jpg', self.frame)[1].tofile(fileNamePicture)
        else:
            self.timer.stop()
            cv2.imencode('.jpg', self.frame)[1].tofile(fileNamePicture)
            self.imagelabel.setPixmap(QPixmap("image/black.png"))
            time.sleep(0.1)
            self.timer.start(20)
        photomessage = "picture successfully saved to " + self.filenameImage
        self.status.showMessage(photomessage, 3000)

    def SaveVideo(self):
        # button-record function
        if self.buttonvideo.isChecked():
            self.fourcc = cv2.VideoWriter_fourcc('M', 'J', 'P', 'G')
            try:
                os.mkdir(f"{self.filenameVideo}\VIDEO_{time.strftime('%Y%m%d%H%M%S', time.localtime())}")
                os.mkdir(f"{self.filenameVideo}\VIDEO_{time.strftime('%Y%m%d%H%M%S', time.localtime())}\plot")
                os.mkdir(f"{self.filenameVideo}\VIDEO_{time.strftime('%Y%m%d%H%M%S', time.localtime())}\csv")
                self.plot_loc = str(
                    f"{self.filenameVideo}\VIDEO_{time.strftime('%Y%m%d%H%M%S', time.localtime())}\plot")
                self.csv_loc = str(f"{self.filenameVideo}\VIDEO_{time.strftime('%Y%m%d%H%M%S', time.localtime())}\csv")
                fileNameVideo = self.filenameVideo + "\VIDEO_" + time.strftime("%Y%m%d%H%M%S", time.localtime()) \
                                + "\VIDEO_" + time.strftime("%Y%m%d%H%M%S", time.localtime()) + ".avi"
                self.R = []
                self.G = []
                self.B = []
                self.Y = []
                self.L = []
                self.V = []
                self.out = cv2.VideoWriter(fileNameVideo, self.fourcc, self.FPS, self.Size)
                self.timerVideo.start(20)
                self.buttonvideo.setText("stop")
                self.status.showMessage("recording……")
            except:
                fileNameVideo = self.filenameVideo + "\VIDEO_" + time.strftime("%Y%m%d%H%M%S", time.localtime()) \
                                + "\VIDEO_" + time.strftime("%Y%m%d%H%M%S", time.localtime()) + ".avi"
                self.R = []
                self.G = []
                self.B = []
                self.Y = []
                self.L = []
                self.V = []
                self.out = cv2.VideoWriter(fileNameVideo, self.fourcc, self.FPS, self.Size)
                self.timerVideo.start(20)
                self.buttonvideo.setText("stop")
                self.status.showMessage("recording……")
        else:
            self.timerVideo.stop()
            self.out.release()
            self.buttonvideo.setText("record")
            videomessage = "video successfully saved to " + self.filenameVideo
            self.status.showMessage(videomessage, 3000)
            self.df = pd.DataFrame({'R': self.R, 'G': self.G, 'B': self.B, 'Y': self.Y, 'L': self.L, 'V': self.V})
            self.df['time'] = (self.df.index + 1) / 15
            self.df.set_index('time', inplace=True)
            plt.plot(self.df.Y, label='Y')
            plt.title("brightness plot")
            plt.xlabel("time (second)")
            plt.ylabel("brightness_value")
            plt.plot(self.df.L, label='L')
            plt.plot(self.df.V, label='V')
            plt.legend()
            plt.savefig(f"{self.plot_loc}\Brightness plot.jpg")
            plt.close()
            try:
                self.df.to_csv(f"{self.csv_loc}\RGBYLV_data.csv")
            except:
                raise PermissionError("close the opened csv first")

    def VideoFrame(self):
        # function looping in the application
        ret, frame = self.camera.read()
        self.out.write(frame)
        if ret:
            self.B.append(frame[:, :, 0].mean())
            self.G.append(frame[:, :, 1].mean())
            self.R.append(frame[:, :, 2].mean())
            self.Y.append(0.299 * frame[:, :, 2].mean() +
                          0.587 * frame[:, :, 1].mean() +
                          0.114 * frame[:, :, 0].mean())
            self.L.append(colorsys.rgb_to_hls(frame[:, :, 2].mean() / 255,
                                              frame[:, :, 1].mean() / 255,
                                              frame[:, :, 0].mean() / 255)[1] * 255)
            self.V.append(colorsys.rgb_to_hsv(frame[:, :, 2].mean() / 255,
                                              frame[:, :, 1].mean() / 255,
                                              frame[:, :, 0].mean() / 255)[2] * 255)


if __name__ == "__main__":
    app = QApplication(
        sys.argv)
    mainUI = YLVP()
    mainUI.show()
    sys.exit(app.exec_())
