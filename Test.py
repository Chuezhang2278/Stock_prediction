# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Test.ui',
# licensing of 'Test.ui' applies.
#
# Created: Mon Nov 18 23:07:27 2019
#      by: pyside2-uic  running on PySide2 5.13.2
#
# WARNING! All changes made in this file will be lost!

from PySide2 import QtCore, QtGui, QtWidgets

class TestWindow(object):
    def setupUi(self, CurrentWindow):
        self.CurrentWindow = CurrentWindow
        CurrentWindow.setObjectName("CurrentWindow")
        CurrentWindow.resize(400, 300)
        self.test_label = QtWidgets.QLabel(CurrentWindow)
        self.test_label.setGeometry(QtCore.QRect(60, 50, 281, 141))
        font = QtGui.QFont()
        font.setPointSize(60)
        self.test_label.setFont(font)
        self.test_label.setAlignment(QtCore.Qt.AlignCenter)
        self.test_label.setObjectName("test_label")
        self.close_button = QtWidgets.QPushButton(CurrentWindow)
        self.close_button.setGeometry(QtCore.QRect(150, 240, 93, 28))
        self.close_button.setObjectName("close_button")

        self.close_button.clicked.connect(self.return_to_parent)
        self.retranslateUi(CurrentWindow)
        QtCore.QMetaObject.connectSlotsByName(CurrentWindow)

    def retranslateUi(self, CurrentWindow):
        CurrentWindow.setWindowTitle(QtWidgets.QApplication.translate("CurrentWindow", "Test Window - Meme Stock Market", None, -1))
        self.test_label.setText(QtWidgets.QApplication.translate("CurrentWindow", "TEST", None, -1))
        self.close_button.setText(QtWidgets.QApplication.translate("CurrentWindow", "Close", None, -1))

    def connectWindows(self, ParentWindow):
        self.ParentWindow = ParentWindow

    def return_to_parent(self):
        self.CurrentWindow.hide()
        self.ParentWindow.show()
