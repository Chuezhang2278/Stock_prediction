# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MemeLogin.ui',
# licensing of 'MemeLogin.ui' applies.
#
# Created: Thu Nov  7 23:03:19 2019
#      by: pyside2-uic  running on PySide2 5.13.2
#
# WARNING! All changes made in this file will be lost!
import sys, icon_rc, qdarkstyle, mysql.connector
from PySide2 import QtCore, QtGui, QtWidgets
from SignUp import SignUpWindow
from MainWindow import MemeWindow

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
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/newPrefix/icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.username_label = QtWidgets.QLabel(self.centralwidget)
        self.username_label.setGeometry(QtCore.QRect(50, 70, 71, 16))
        self.username_label.setObjectName("username_label")
        self.password_label = QtWidgets.QLabel(self.centralwidget)
        self.password_label.setGeometry(QtCore.QRect(50, 100, 71, 20))
        self.password_label.setObjectName("password_label")
        self.username_edit = QtWidgets.QLineEdit(self.centralwidget)
        self.username_edit.setGeometry(QtCore.QRect(130, 70, 261, 22))
        self.username_edit.setStyleSheet("")
        self.username_edit.setObjectName("username_edit")
        self.password_edit = QtWidgets.QLineEdit(self.centralwidget)
        self.password_edit.setGeometry(QtCore.QRect(130, 100, 261, 22))
        self.password_edit.setObjectName("password_edit")
        self.password_edit.setEchoMode(QtWidgets.QLineEdit.Password);
        self.login_button = QtWidgets.QPushButton(self.centralwidget)
        self.login_button.setGeometry(QtCore.QRect(250, 160, 93, 28))
        self.login_button.setObjectName("login_button")
        self.signup_button = QtWidgets.QPushButton(self.centralwidget)
        self.signup_button.setGeometry(QtCore.QRect(130, 160, 93, 28))
        self.signup_button.setObjectName("signup_button")
        self.username_label_4 = QtWidgets.QLabel(self.centralwidget)
        self.username_label_4.setGeometry(QtCore.QRect(394, 0, 71, 71))
        self.username_label_4.setText("")
        self.username_label_4.setPixmap(QtGui.QPixmap(":/newPrefix/icon.png"))
        self.username_label_4.setObjectName("username_label_4")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.signup_button.clicked.connect(self.signup)
        self.login_button.clicked.connect(self.login)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtWidgets.QApplication.translate("MainWindow", "Log In - Meme Stock Market", None, -1))
        self.username_label.setText(QtWidgets.QApplication.translate("MainWindow", "Username:", None, -1))
        self.password_label.setText(QtWidgets.QApplication.translate("MainWindow", "Password:", None, -1))
        self.login_button.setText(QtWidgets.QApplication.translate("MainWindow", "Login", None, -1))
        self.signup_button.setText(QtWidgets.QApplication.translate("MainWindow", "Sign Up", None, -1))

    def signup(self):
        self.SignUpWindow = QtWidgets.QMainWindow()
        self.ui = SignUpWindow()
        self.ui.setupUi(self.SignUpWindow)
        self.SignUpWindow.show()
        MainWindow.hide()

    def login(self):
        username_text = self.username_edit.text()
        password_text = self.password_edit.text()

        mydb = mysql.connector.connect(
            host='localhost',
            user='root',
            password='123password',
            database='memestock')

        mycursor = mydb.cursor()
        # check how this library does user input
        # check how string equality work

        mycursor.execute("SELECT username, pass FROM users WHERE username = %s AND pass = %s", (username_text, password_text))
        usercheck = mycursor.fetchone()
        if(usercheck != None and usercheck[0] == username_text and usercheck[1] == password_text):
            print("Login Success!")
            self.SignUpWindow = QtWidgets.QMainWindow()
            self.ui = MemeWindow()
            self.ui.setupUi(self.SignUpWindow)
            MainWindow.hide()
            self.SignUpWindow.show()
        else:
            print("Login Failed!")


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    app.setWindowIcon(QtGui.QIcon("UI_Folder/icon.png"))
    MainWindow = QtWidgets.QMainWindow()
    ui = LoginWindow()
    ui.setupUi(MainWindow)
    app.setStyleSheet(qdarkstyle.load_stylesheet_pyqt5())
    MainWindow.show()
    sys.exit(app.exec_())
