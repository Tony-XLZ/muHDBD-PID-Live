import matplotlib
matplotlib.use("Qt5Agg")

from PyQt5.QtWidgets import QVBoxLayout, QSizePolicy, QWidget
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
import matplotlib.pyplot as plt


class MyMplCanvas(FigureCanvas):
    def __init__(self, parent=None, width=5, height=4, dpi=100):
        plt.rcParams['axes.unicode_minus'] = False  # show minus normally

        self.fig = Figure(figsize=(width, height), dpi=dpi)
        self.axes = self.fig.add_subplot(111)
        self.fig.subplots_adjust(left=0.180, bottom=0.110, right=0.990, top=0.990,wspace=None, hspace=None)

        FigureCanvas.__init__(self, self.fig)
        self.setParent(parent)

        FigureCanvas.setSizePolicy(self, QSizePolicy.Expanding, QSizePolicy.Expanding)

        FigureCanvas.updateGeometry(self)

    def plot(self, histr=[0]):
        # plot function
        self.axes.cla()
        self.axes.plot(histr)
        self.axes.set_ylabel('Pixel')
        self.axes.set_xlabel('Grey Scale')
        self.axes.set_xlim((0,256))
        self.draw()


class MatplotlibWidget(QWidget):
    def __init__(self, parent=None):
        super(MatplotlibWidget, self).__init__(parent)
        self.initUi()

    def initUi(self):
        self.layout = QVBoxLayout(self)
        self.histMP = MyMplCanvas(self, width=3.78, height=3.86, dpi=100)
        self.layout.addWidget(self.histMP)