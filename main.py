from gui import Ui_MainWindow
from data_capture import Sniffer
from data_consume import Consumer
from PyQt5.Qt import *
from PyQt5 import QtCore
from queue import Queue
import sys
import pyqtgraph as pg


class MyApp(QMainWindow,Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.que = Queue()
        self.sniffer = Sniffer(self.que)
        self.consumer = Consumer(self.que)
        self.startButton.clicked.connect(self.onStartBtnClicked)
        self.initPlotWindow()

    def initPlotWindow(self):

        self.timer = QtCore.QTimer()
        self.timer.setInterval(0)  # ASAP
        self.timer.timeout.connect(self.update_plot_data)
        self.curve = self.graphicsView.plot(pen=pg.mkPen('r', width=1))
        self.graphicsView.setBackground('w')
        self.graphicsView.setYRange(min=-255,max=255,padding=0)
        # self.graphicsView.setXRange(min=0,max=1000,padding=0)

    def onStartBtnClicked(self):
        self.sniffer.start()
        self.consumer.start()
        self.timer.start()

    def update_plot_data(self):
        # self.graphicsView.clear()
        self.curve.setData(self.consumer.channels[0,:])

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())
