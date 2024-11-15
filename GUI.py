from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1005, 554)
        MainWindow.setMinimumSize(QtCore.QSize(10, 10))
        MainWindow.setToolTip("")
        MainWindow.setStatusTip("")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.layoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget.setGeometry(QtCore.QRect(0, 0, 1301, 523))
        self.layoutWidget.setObjectName("layoutWidget")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.layoutWidget)
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.verticalLayout_3.addLayout(self.gridLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_hist = QtWidgets.QLabel(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_hist.sizePolicy().hasHeightForWidth())
        self.label_hist.setSizePolicy(sizePolicy)
        self.label_hist.setMinimumSize(QtCore.QSize(100, 20))
        self.label_hist.setMaximumSize(QtCore.QSize(16777215, 20))
        self.label_hist.setObjectName("label_hist")
        self.horizontalLayout_2.addWidget(self.label_hist)
        spacerItem = QtWidgets.QSpacerItem(138, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.verticalLayout_3.addLayout(self.horizontalLayout_2)
        self.histWidget = MatplotlibWidget(self.layoutWidget)
        self.histWidget.setMinimumSize(QtCore.QSize(378, 370))
        self.histWidget.setObjectName("histWidget")
        self.verticalLayout_3.addWidget(self.histWidget)
        self.horizontalLayout_4.addLayout(self.verticalLayout_3)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_cam = QtWidgets.QLabel(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_cam.sizePolicy().hasHeightForWidth())
        self.label_cam.setSizePolicy(sizePolicy)
        self.label_cam.setMinimumSize(QtCore.QSize(100, 20))
        self.label_cam.setObjectName("label_cam")
        self.verticalLayout.addWidget(self.label_cam)
        self.imagelabel = QtWidgets.QLabel(self.layoutWidget)
        self.imagelabel.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.imagelabel.sizePolicy().hasHeightForWidth())
        self.imagelabel.setSizePolicy(sizePolicy)
        self.imagelabel.setMinimumSize(QtCore.QSize(610, 453))
        self.imagelabel.setMaximumSize(QtCore.QSize(610, 453))
        self.imagelabel.setText("")
        self.imagelabel.setPixmap(QtGui.QPixmap("source/nonentity.png"))
        self.imagelabel.setScaledContents(True)
        self.imagelabel.setAlignment(QtCore.Qt.AlignCenter)
        self.imagelabel.setObjectName("imagelabel")
        self.verticalLayout.addWidget(self.imagelabel)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.buttonChoose = QtWidgets.QPushButton(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.buttonChoose.sizePolicy().hasHeightForWidth())
        self.buttonChoose.setSizePolicy(sizePolicy)
        self.buttonChoose.setMinimumSize(QtCore.QSize(80, 23))
        self.buttonChoose.setMaximumSize(QtCore.QSize(1888, 223445))
        self.buttonChoose.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.buttonChoose.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.buttonChoose.setObjectName("buttonChoose")
        self.horizontalLayout_3.addWidget(self.buttonChoose)
        spacerItem1 = QtWidgets.QSpacerItem(388, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem1)
        self.ButtonStop = QtWidgets.QPushButton(self.layoutWidget)
        self.ButtonStop.setMinimumSize(QtCore.QSize(60, 26))
        self.ButtonStop.setMaximumSize(QtCore.QSize(50, 16777215))
        self.ButtonStop.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.ButtonStop.setCheckable(True)
        self.ButtonStop.setObjectName("ButtonStop")
        self.horizontalLayout_3.addWidget(self.ButtonStop)
        self.buttonvideo = QtWidgets.QPushButton(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.buttonvideo.sizePolicy().hasHeightForWidth())
        self.buttonvideo.setSizePolicy(sizePolicy)
        self.buttonvideo.setMinimumSize(QtCore.QSize(60, 23))
        self.buttonvideo.setMaximumSize(QtCore.QSize(60, 30))
        self.buttonvideo.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.buttonvideo.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.buttonvideo.setCheckable(True)
        self.buttonvideo.setChecked(False)
        self.buttonvideo.setObjectName("buttonvideo")
        self.horizontalLayout_3.addWidget(self.buttonvideo)
        self.buttoncamera = QtWidgets.QPushButton(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.buttoncamera.sizePolicy().hasHeightForWidth())
        self.buttoncamera.setSizePolicy(sizePolicy)
        self.buttoncamera.setMinimumSize(QtCore.QSize(60, 23))
        self.buttoncamera.setMaximumSize(QtCore.QSize(60, 30))
        self.buttoncamera.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.buttoncamera.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.buttoncamera.setObjectName("buttoncamera")
        self.horizontalLayout_3.addWidget(self.buttoncamera)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_4.addLayout(self.verticalLayout)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem2)
        self.imageLabel_edge = QtWidgets.QLabel(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.imageLabel_edge.sizePolicy().hasHeightForWidth())
        self.imageLabel_edge.setSizePolicy(sizePolicy)
        self.imageLabel_edge.setMinimumSize(QtCore.QSize(300, 225))
        self.imageLabel_edge.setMaximumSize(QtCore.QSize(300, 225))
        self.imageLabel_edge.setText("")
        self.imageLabel_edge.setPixmap(QtGui.QPixmap("source/nonentity.png"))
        self.imageLabel_edge.setScaledContents(True)
        self.imageLabel_edge.setAlignment(QtCore.Qt.AlignCenter)
        self.imageLabel_edge.setObjectName("imageLabel_edge")
        self.verticalLayout_2.addWidget(self.imageLabel_edge)
        self.horizontalLayout_4.addLayout(self.verticalLayout_2)
        MainWindow.setCentralWidget(self.centralwidget)
        self.status = QtWidgets.QStatusBar(MainWindow)
        self.status.setObjectName("status")
        MainWindow.setStatusBar(self.status)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "μHD-PID Live"))
        self.label_hist.setText(_translate("MainWindow", " Histogram"))
        self.label_cam.setText(_translate("MainWindow", "Camera"))
        self.buttonChoose.setText(_translate("MainWindow", "switch cam"))
        self.ButtonStop.setText(_translate("MainWindow", "pause"))
        self.buttonvideo.setText(_translate("MainWindow", "record"))
        self.buttoncamera.setText(_translate("MainWindow", "capture"))


from MatplotlibWidget import MatplotlibWidget