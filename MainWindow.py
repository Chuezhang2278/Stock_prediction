# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'CurrentWindow.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!

import sys, icon_rc, qdarkstyle, datetime
import pandas as pd
import matplotlib.pyplot as plt
from pandas_datareader import data as data, wb
from PySide2 import QtCore, QtGui, QtWidgets
from StockWindow import StockWindow

class MemeWindow(object):
    def setupUi(self, CurrentWindow):
        self.CurrentWindow = CurrentWindow
        CurrentWindow.setObjectName("CurrentWindow")
        CurrentWindow.resize(707, 496)
        self.centralwidget = QtWidgets.QWidget(CurrentWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(20, 30, 581, 391))
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.tabWidget.addTab(self.tab_2, "")
        CurrentWindow.setCentralWidget(self.centralwidget)
        self.test_button = QtWidgets.QPushButton(self.centralwidget)
        self.test_button.setGeometry(QtCore.QRect(250, 160, 93, 28))
        self.test_button.setObjectName("test")

        self.test_button.clicked.connect(self.test_click)
        self.retranslateUi(CurrentWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(CurrentWindow)

    def retranslateUi(self, CurrentWindow):
        _translate = QtCore.QCoreApplication.translate
        CurrentWindow.setWindowTitle(_translate("CurrentWindow", "Main Window - Meme Stock Market"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("CurrentWindow", "Tab 1"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("CurrentWindow", "Tab 2"))
        self.test_button.setText(QtWidgets.QApplication.translate("CurrentWindow", "Test", None, -1))

    def test_click(self):
        end = datetime.datetime.today()
        start = end + datetime.timedelta(days=-365)
        df = data.DataReader("AMD", 'yahoo', start, end)
        print (df.to_string())
        df.index=pd.to_datetime(df.index)
        df['High'].plot(cmap='RdBu', xlim=[pd.Timestamp(start), pd.Timestamp(end)])
        plt.suptitle("AMD Stocks: from " + start.strftime('%m/%d/%Y') + " to " + end.strftime('%m/%d/%Y'))
        plt.ylabel("High (USD)", fontdict=None, labelpad=None)
        plt.show()
        #self.StockWindow = QtWidgets.QMainWindow()
        #self.temp = StockWindow()
        #self.temp.connectWindows(self.CurrentWindow)
        #self.temp.setupUi(self.StockWindow)
        #self.StockWindow.show()
        #self.CurrentWindow.hide()

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    CurrentWindow = QtWidgets.QMainWindow()
    ui = MemeWindow()
    ui.setupUi(CurrentWindow)
    CurrentWindow.show()
    sys.exit(app.exec_())
