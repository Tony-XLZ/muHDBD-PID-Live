from PyQt5 import QtCore, QtGui, QtWidgets
from MatplotlibWidget import MatplotlibWidget

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1200, 523)
        MainWindow.setMinimumSize(QtCore.QSize(660, 240))
        self.centralwidget = QtWidgets.QWidget(MainWindow)

        # Main Layout as a Splitter
        self.mainSplitter = QtWidgets.QSplitter(self.centralwidget)
        self.mainSplitter.setOrientation(QtCore.Qt.Horizontal)

        # Left Section - Histogram
        self.setupHistogramSection()

        # Right Section - Camera and Buttons
        self.setupCameraSection()

        # Set Main Layout
        mainLayout = QtWidgets.QHBoxLayout(self.centralwidget)
        mainLayout.addWidget(self.mainSplitter)
        MainWindow.setCentralWidget(self.centralwidget)

        # Status Bar
        self.status = QtWidgets.QStatusBar(MainWindow)
        MainWindow.setStatusBar(self.status)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def setupHistogramSection(self):
        self.histogramWidget = QtWidgets.QWidget()
        histogramLayout = QtWidgets.QVBoxLayout(self.histogramWidget)

        # Histogram Label
        self.label_hist = QtWidgets.QLabel("Histogram")
        self.label_hist.setSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        self.label_hist.setMinimumSize(QtCore.QSize(100, 20))
        histogramLayout.addWidget(self.label_hist)

        # Matplotlib Widget for Histogram
        self.histWidget = MatplotlibWidget(self.centralwidget)
        self.histWidget.setMinimumSize(QtCore.QSize(400, 400))
        histogramLayout.addWidget(self.histWidget)

        # Add to main splitter
        self.mainSplitter.addWidget(self.histogramWidget)

    def setupCameraSection(self):
        self.cameraWidget = QtWidgets.QWidget()
        cameraLayout = QtWidgets.QVBoxLayout(self.cameraWidget)

        # Camera Label
        self.label_cam = QtWidgets.QLabel("Camera")
        self.label_cam.setSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        self.label_cam.setMinimumSize(QtCore.QSize(100, 20))
        cameraLayout.addWidget(self.label_cam)

        # Image Display
        self.imagelabel = QtWidgets.QLabel()
        self.imagelabel.setSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        self.imagelabel.setMinimumSize(QtCore.QSize(400, 300))
        self.imagelabel.setPixmap(QtGui.QPixmap("source/nonentity.png"))
        self.imagelabel.setScaledContents(True)
        self.imagelabel.setAlignment(QtCore.Qt.AlignCenter)
        cameraLayout.addWidget(self.imagelabel)

        # Control Buttons Layout (below camera)
        controlLayout = QtWidgets.QHBoxLayout()

        # Button: Switch Camera
        self.buttonChoose = QtWidgets.QPushButton("Switch Cam")
        self.buttonChoose.setMinimumSize(QtCore.QSize(80, 23))
        self.buttonChoose.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        controlLayout.addWidget(self.buttonChoose)

        # Spacer to push the other buttons to the right
        controlLayout.addStretch()

        # Button: Pause
        self.ButtonStop = QtWidgets.QPushButton("Pause")
        self.ButtonStop.setMinimumSize(QtCore.QSize(60, 23))
        self.ButtonStop.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.ButtonStop.setCheckable(True)
        controlLayout.addWidget(self.ButtonStop)

        # Button: Record
        self.buttonvideo = QtWidgets.QPushButton("Record")
        self.buttonvideo.setMinimumSize(QtCore.QSize(60, 23))
        self.buttonvideo.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.buttonvideo.setCheckable(True)
        controlLayout.addWidget(self.buttonvideo)

        # Button: Capture
        self.buttoncamera = QtWidgets.QPushButton("Capture")
        self.buttoncamera.setMinimumSize(QtCore.QSize(60, 23))
        self.buttoncamera.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        controlLayout.addWidget(self.buttoncamera)

        # Add the control buttons layout below the camera image
        cameraLayout.addLayout(controlLayout)

        # Add to main splitter
        self.mainSplitter.addWidget(self.cameraWidget)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "μHD-PID Live"))


from MatplotlibWidget import MatplotlibWidget
