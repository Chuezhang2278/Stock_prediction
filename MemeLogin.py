# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MemeLogin.ui',
# licensing of 'MemeLogin.ui' applies.
#
# Created: Thu Nov  7 23:03:19 2019
#      by: pyside2-uic  running on PySide2 5.13.2
#
# WARNING! All changes made in this file will be lost!
import sys, icon_rc, qdarkstyle
from PySide2 import QtCore, QtGui, QtWidgets

class LoginWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setEnabled(True)
        MainWindow.resize(461, 253)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QtCore.QSize(461, 253))
        MainWindow.setMaximumSize(QtCore.QSize(461, 253))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(50, 70, 71, 16))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(50, 100, 71, 20))
        self.label_2.setObjectName("label_2")
        self.Username_lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.Username_lineEdit.setGeometry(QtCore.QRect(130, 70, 261, 22))
        self.Username_lineEdit.setStyleSheet("")
        self.Username_lineEdit.setObjectName("Username_lineEdit")
        self.password_LineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.password_LineEdit.setGeometry(QtCore.QRect(130, 100, 261, 22))
        self.password_LineEdit.setObjectName("password_LineEdit")
        self.Login_Button = QtWidgets.QPushButton(self.centralwidget)
        self.Login_Button.setGeometry(QtCore.QRect(250, 160, 93, 28))
        self.Login_Button.setObjectName("Login_Button")
        self.SignUp_Button = QtWidgets.QPushButton(self.centralwidget)
        self.SignUp_Button.setGeometry(QtCore.QRect(130, 160, 93, 28))
        self.SignUp_Button.setObjectName("SignUp_Button")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(394, 0, 71, 71))
        self.label_4.setText("")
        self.label_4.setPixmap(QtGui.QPixmap(":/newPrefix/icon.png"))
        self.label_4.setObjectName("label_4")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtWidgets.QApplication.translate("MainWindow", "Log In - Meme Stock Market", None, -1))
        self.label.setText(QtWidgets.QApplication.translate("MainWindow", "Username:", None, -1))
        self.label_2.setText(QtWidgets.QApplication.translate("MainWindow", "Password:", None, -1))
        self.Login_Button.setText(QtWidgets.QApplication.translate("MainWindow", "Login", None, -1))
        self.SignUp_Button.setText(QtWidgets.QApplication.translate("MainWindow", "Sign Up", None, -1))

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    app.setWindowIcon(QtGui.QIcon("UI_Folder/icon.png"))
    MainWindow = QtWidgets.QMainWindow()
    ui = LoginWindow()
    ui.setupUi(MainWindow)
    app.setStyleSheet(qdarkstyle.load_stylesheet_pyqt5())
    MainWindow.show()
    sys.exit(app.exec_())
