# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'CurrentWindow.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!

import sys, icon_rc, qdarkstyle, datetime
from PyQt5 import QtCore, QtGui, QtWidgets
from StockWindow import StockWindow
from pandas_datareader import data as data, wb

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

        #TEST STUFF
        self.stock_button = QtWidgets.QPushButton(self.centralwidget)
        self.stock_button.setGeometry(QtCore.QRect(250, 160, 93, 28))
        self.stock_button.setObjectName("stock_button")
        self.stock_button.clicked.connect(self.stock_click)
        self.stock_edit = QtWidgets.QLineEdit(CurrentWindow)
        self.stock_edit.setGeometry(QtCore.QRect(230, 200, 131, 31))
        self.stock_edit.setText("")
        self.stock_edit.setObjectName("stock_edit")
        self.high_label = QtWidgets.QLabel(CurrentWindow)
        self.high_label.setGeometry(QtCore.QRect(175, 250, 250, 150))
        self.high_label.setStyleSheet("background-color: #445661; border-radius: 5px;")
        self.high_label.setObjectName("high_label")
        self.high_label.setText("Hey cutie, please enter a legit stock ID :)\nYou can use anything you want\nHere are some examples: \n'AMZN' for Amazon \n'M' for Macys \n'AAPL' for Apple \n'AMD' for AMD \n'INTC' for Intel")
        #TEST STUFF
        self.retranslateUi(CurrentWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(CurrentWindow)

    def retranslateUi(self, CurrentWindow):
        _translate = QtCore.QCoreApplication.translate
        CurrentWindow.setWindowTitle(_translate("CurrentWindow", "Main Window"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("CurrentWindow", "Tab 1"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("CurrentWindow", "Tab 2"))
        self.stock_button.setText(QtWidgets.QApplication.translate("CurrentWindow", "Stock", None, -1))

    def stock_click(self):
        try:
            data.DataReader(self.stock_edit.text(), 'yahoo')
        except:
            self.high_label.setText("Enter a legit company stock ID >.<")
        else:
            self.StockWindow = QtWidgets.QMainWindow()
            self.ui = StockWindow(self.stock_edit.text(), 0)
            self.ui.connectWindows(self.CurrentWindow)
            self.ui.setupUi(self.StockWindow)
            self.StockWindow.show()
            self.CurrentWindow.hide()
            self.high_label.setText("Hey cutie, please enter a legit stock ID :)  \n'AMZN' for Amazon \n'M' for Macys \n'AAPL' for Apple \n'AMD' for AMD \n'INTC' for Intel")

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    app.setWindowIcon(QtGui.QIcon("UI_Folder/icon.png"))
    app.setStyleSheet(qdarkstyle.load_stylesheet_pyqt5())
    CurrentWindow = QtWidgets.QMainWindow()
    ui = MemeWindow()
    ui.setupUi(CurrentWindow)
    CurrentWindow.show()
    sys.exit(app.exec_())
