import sys
import pyqtgraph as pg
import numpy as np
from PyQt4 import QtGui, QtCore

app = pg.mkQApp()

class PW(QtGui.QWidget):
    def __init__(self):
        QtGui.QWidget.__init__(self)
        self.resize(650, 650)
        self.setWindowTitle("Graph in Widget")

        self.layout = QtGui.QGridLayout()
        self.setLayout(self.layout)

        self.plot = pg.PlotWidget(title="Random Plotting")
        self.layout.addWidget(self.plot)

        self.plot_button = QtGui.QPushButton("Start", self)
        self.plot_button.clicked.connect(self.plotGraph)
        self.layout.addWidget(self.plot_button, 2, 0)

        self.save_button = QtGui.QPushButton("Save", self)
        self.save_button.clicked.connect(self.plotGraph)
        self.layout.addWidget(self.save_button, 3, 0)

        self.quit_button = QtGui.QPushButton("Quit", self)
        self.quit_button.clicked.connect(self.plotGraph)
        self.layout.addWidget(self.quit_button, 4, 0)

    def plotGraph(self):
        self.plot.clear()
        pg.setConfigOptions(antialias=True)

        self.data = np.random.normal(loc=0.0, scale=2, size=100)
        #self.plot.plotItem.plot(self.data)
        curve1 = self.plot.plotItem.plot(self.data)
        #curve2 = self.plot.plotItem.plot(self.data)

        self.ptr = 1
        
        def update():
            #self.plot.clear()
            ##self.data = np.roll(self.data, 1)  # scroll data
            ##curve1.setData(self.data)
            print self.data
            self.data[:-1] = self.data[1:]  # shift data in the array one sample left # (see also: np.roll)
            self.data[-1] = np.random.normal()
            print self.data
            curve1.setData(self.data)
            #curve1.setPos(self.ptr, 0)
            #self.ptr += 1

##        def update1(curve1, curve2, ptr):
##            #global curve1, ptr1
##            self.data[:-1] = self.data[1:]  # shift data in the array one sample left # (see also: np.roll)
##            self.data[-1] = np.random.normal()
##            curve1.setData(self.data)
##    
##            ptr += 1
##            curve2.setData(self.data)
##            curve2.setPos(ptr, 0)

        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(update)
        self.timer.start(1000)


plotter = PW()
plotter.show()

sys.exit(app.exec_())
