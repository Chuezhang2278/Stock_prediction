# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Error.ui',
# licensing of 'Error.ui' applies.
#
# Created: Sun Nov 17 21:45:30 2019
#      by: pyside2-uic  running on PySide2 5.13.2
#
# WARNING! All changes made in this file will be lost!

import sys, icon_rc, qdarkstyle
from PyQt5 import QtCore, QtGui, QtWidgets

class ErrorWindow(object):
    def setupUi(self, CurrentWindow):
        self.CurrentWindow = CurrentWindow
        CurrentWindow.setObjectName("CurrentWindow")
        CurrentWindow.resize(482, 444)
        CurrentWindow.setMinimumSize(QtCore.QSize(482, 444))
        CurrentWindow.setMaximumSize(QtCore.QSize(482, 444))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        font.setPointSize(10)
        CurrentWindow.setFont(font)
        self.error_label = QtWidgets.QLabel(CurrentWindow)
        self.error_label.setGeometry(QtCore.QRect(176, 50, 130, 51))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        font.setPointSize(22)
        font.setWeight(50)
        font.setBold(False)
        self.error_label.setFont(font)
        self.error_label.setStyleSheet("background-color: #32414b; border-radius: 10px;")
        self.error_label.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.error_label.setFrameShadow(QtWidgets.QFrame.Plain)
        self.error_label.setLineWidth(1)
        self.error_label.setTextFormat(QtCore.Qt.AutoText)
        self.error_label.setAlignment(QtCore.Qt.AlignCenter)
        self.error_label.setMargin(0)
        self.error_label.setObjectName("error_label")
        self.line1 = QtWidgets.QLabel(CurrentWindow)
        self.line1.setGeometry(QtCore.QRect(80, 130, 391, 31))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        font.setPointSize(8)
        self.line1.setFont(font)
        self.line1.setObjectName("line1")
        self.line2 = QtWidgets.QLabel(CurrentWindow)
        self.line2.setGeometry(QtCore.QRect(110, 170, 321, 31))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        font.setPointSize(8)
        self.line2.setFont(font)
        self.line2.setObjectName("line2")
        self.line3 = QtWidgets.QLabel(CurrentWindow)
        self.line3.setGeometry(QtCore.QRect(80, 210, 391, 31))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        font.setPointSize(8)
        self.line3.setFont(font)
        self.line3.setObjectName("line3")
        self.line4 = QtWidgets.QLabel(CurrentWindow)
        self.line4.setGeometry(QtCore.QRect(130, 250, 271, 31))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        font.setPointSize(8)
        self.line4.setFont(font)
        self.line4.setObjectName("line4")
        self.line5 = QtWidgets.QLabel(CurrentWindow)
        self.line5.setGeometry(QtCore.QRect(120, 290, 291, 31))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        font.setPointSize(8)
        self.line5.setFont(font)
        self.line5.setObjectName("line5")
        self.close_button = QtWidgets.QPushButton(CurrentWindow)
        self.close_button.setGeometry(QtCore.QRect(180, 380, 111, 31))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.close_button.setFont(font)
        self.close_button.setObjectName("close_button")
        self.close_button.clicked.connect(self.close_window)
        self.label_4 = QtWidgets.QLabel(CurrentWindow)
        self.label_4.setGeometry(QtCore.QRect(415, 0, 71, 71))
        self.label_4.setText("")
        self.label_4.setPixmap(QtGui.QPixmap(":/newPrefix/icon.png"))
        self.label_4.setObjectName("label_4")
        self.line5_2 = QtWidgets.QLabel(CurrentWindow)
        self.line5_2.setGeometry(QtCore.QRect(90, 330, 291, 31))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        font.setPointSize(8)
        self.line5_2.setFont(font)
        self.line5_2.setObjectName("line5_2")

        self.retranslateUi(CurrentWindow)
        QtCore.QMetaObject.connectSlotsByName(CurrentWindow)

    def retranslateUi(self, CurrentWindow):
        CurrentWindow.setWindowTitle(QtWidgets.QApplication.translate("CurrentWindow", "Sign Up Error", None, -1))
        self.error_label.setText(QtWidgets.QApplication.translate("CurrentWindow", "Error", None, -1))
        self.line1.setText(QtWidgets.QApplication.translate("CurrentWindow", "E-mail must contain @ and .com or .edu at the end", None, -1))
        self.line2.setText(QtWidgets.QApplication.translate("CurrentWindow", "Social security number must be 9 digits", None, -1))
        self.line3.setText(QtWidgets.QApplication.translate("CurrentWindow", "Password must be at least 9 characters", None, -1))
        self.line4.setText(QtWidgets.QApplication.translate("CurrentWindow", "Please make sure all fields are filled", None, -1))
        self.line5.setText(QtWidgets.QApplication.translate("CurrentWindow", "Username and e-mail must be unique", None, -1))
        self.close_button.setText(QtWidgets.QApplication.translate("CurrentWindow", "Close", None, -1))
        self.line5_2.setText(QtWidgets.QApplication.translate("CurrentWindow", "Username and password may not have spaces", None, -1))

    def close_window(self):
        self.CurrentWindow.hide()

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    app.setWindowIcon(QtGui.QIcon("UI_Folder/icon.png"))
    MainWindow = QtWidgets.QMainWindow()
    ui = ErrorWindow()
    ui.setupUi(MainWindow)
    app.setStyleSheet(qdarkstyle.load_stylesheet_pyqt5())
    MainWindow.show()
    sys.exit(app.exec_())
