# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'SignUp.ui',
# licensing of 'SignUp.ui' applies.
#
# Created: Thu Nov  7 23:03:41 2019
#      by: pyside2-uic  running on PySide2 5.13.2
#
# WARNING! All changes made in this file will be lost!
import sys, icon_rc, qdarkstyle, mysql.connector, DatabaseConnect as db
from PyQt5 import QtCore, QtGui, QtWidgets
from ErrorWindow import ErrorWindow

class SignUpWindow(object):
    def __init__(self):
        self.CurrentWindow = None;
        self.LoginWindow = None;

    def setupUi(self, CurrentWindow, LoginWindow):
        self.LoginWindow = LoginWindow
        self.CurrentWindow = CurrentWindow
        self.CurrentWindow.setObjectName("CurrentWindow")
        self.CurrentWindow.resize(446, 306)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(CurrentWindow.sizePolicy().hasHeightForWidth())
        self.CurrentWindow.setSizePolicy(sizePolicy)
        self.CurrentWindow.setMinimumSize(QtCore.QSize(446, 306))
        self.CurrentWindow.setMaximumSize(QtCore.QSize(446, 306))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/newPrefix/icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.CurrentWindow.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(self.CurrentWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.fullname_label = QtWidgets.QLabel(self.centralwidget)
        self.fullname_label.setGeometry(QtCore.QRect(60, 60, 71, 16))
        self.fullname_label.setObjectName("fullname_label")
        self.ssn_label = QtWidgets.QLabel(self.centralwidget)
        self.ssn_label.setGeometry(QtCore.QRect(60, 90, 55, 16))
        self.ssn_label.setObjectName("ssn_label")
        self.username_label = QtWidgets.QLabel(self.centralwidget)
        self.username_label.setGeometry(QtCore.QRect(60, 120, 71, 16))
        self.username_label.setObjectName("username_label")
        self.pass_label = QtWidgets.QLabel(self.centralwidget)
        self.pass_label.setGeometry(QtCore.QRect(60, 150, 71, 16))
        self.pass_label.setObjectName("pass_label")
        self.email_label = QtWidgets.QLabel(self.centralwidget)
        self.email_label.setGeometry(QtCore.QRect(60, 180, 61, 16))
        self.email_label.setObjectName("email_label")
        self.fullname_edit = QtWidgets.QLineEdit(self.centralwidget)
        self.fullname_edit.setGeometry(QtCore.QRect(140, 60, 221, 22))
        self.fullname_edit.setObjectName("fullname_edit")
        self.ssn_edit = QtWidgets.QLineEdit(self.centralwidget)
        self.ssn_edit.setGeometry(QtCore.QRect(140, 90, 221, 22))
        self.ssn_edit.setObjectName("ssn_edit")
        self.username_edit = QtWidgets.QLineEdit(self.centralwidget)
        self.username_edit.setGeometry(QtCore.QRect(140, 120, 221, 22))
        self.username_edit.setObjectName("username_edit")
        self.pass_edit = QtWidgets.QLineEdit(self.centralwidget)
        self.pass_edit.setGeometry(QtCore.QRect(140, 150, 221, 22))
        self.pass_edit.setObjectName("pass_edit")
        self.email_edit = QtWidgets.QLineEdit(self.centralwidget)
        self.email_edit.setGeometry(QtCore.QRect(140, 180, 221, 22))
        self.email_edit.setObjectName("email_edit")
        self.finish_button = QtWidgets.QPushButton(self.centralwidget)
        self.finish_button.setGeometry(QtCore.QRect(180, 240, 93, 28))
        self.finish_button.setObjectName("finish_button")
        self.gender_label = QtWidgets.QLabel(self.centralwidget)
        self.gender_label.setGeometry(QtCore.QRect(60, 210, 61, 16))
        self.gender_label.setObjectName("gender_label")
        self.maleRadio = QtWidgets.QRadioButton(self.centralwidget)
        self.maleRadio.setGeometry(QtCore.QRect(140, 210, 95, 20))
        self.maleRadio.setObjectName("maleRadio")
        self.femaleRadio = QtWidgets.QRadioButton(self.centralwidget)
        self.femaleRadio.setGeometry(QtCore.QRect(205, 210, 95, 20))
        self.femaleRadio.setObjectName("femaleRadio")
        self.nonbinaryradio = QtWidgets.QRadioButton(self.centralwidget)
        self.nonbinaryradio.setGeometry(QtCore.QRect(283, 210, 95, 20))
        self.nonbinaryradio.setObjectName("nonbinaryradio")
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(378, 0, 71, 71))
        self.label_8.setText("")
        self.label_8.setPixmap(QtGui.QPixmap(":/newPrefix/icon.png"))
        self.label_8.setObjectName("label_8")
        self.CurrentWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(CurrentWindow)
        self.statusbar.setObjectName("statusbar")
        self.CurrentWindow.setStatusBar(self.statusbar)

        self.retranslateUi(self.CurrentWindow)
        QtCore.QMetaObject.connectSlotsByName(self.CurrentWindow)

        self.finish_button.clicked.connect(self.add_user)

    def show_error(self):
        self.ErrorWindow = QtWidgets.QMainWindow()
        self.ui = ErrorWindow()
        self.ui.setupUi(self.ErrorWindow)
        self.ErrorWindow.show()

    def retranslateUi(self, CurrentWindow):
        self.CurrentWindow.setWindowTitle(QtWidgets.QApplication.translate("CurrentWindow", "Sign Up - Meme Stock Market", None, -1))
        self.fullname_label.setText(QtWidgets.QApplication.translate("CurrentWindow", "Full Name:", None, -1))
        self.ssn_label.setText(QtWidgets.QApplication.translate("CurrentWindow", "SSN:", None, -1))
        self.username_label.setText(QtWidgets.QApplication.translate("CurrentWindow", "Username:", None, -1))
        self.pass_label.setText(QtWidgets.QApplication.translate("CurrentWindow", "Password:", None, -1))
        self.email_label.setText(QtWidgets.QApplication.translate("CurrentWindow", "Email:", None, -1))
        self.finish_button.setText(QtWidgets.QApplication.translate("CurrentWindow", "Finish", None, -1))
        self.gender_label.setText(QtWidgets.QApplication.translate("CurrentWindow", "Gender:", None, -1))
        self.maleRadio.setText(QtWidgets.QApplication.translate("CurrentWindow", "Male", None, -1))
        self.femaleRadio.setText(QtWidgets.QApplication.translate("CurrentWindow", "Female", None, -1))
        self.nonbinaryradio.setText(QtWidgets.QApplication.translate("CurrentWindow", "Non-Binary", None, -1))

    def add_user(self):
        mydb = db.mydb
        fullname = self.fullname_edit.text()
        ssn = self.ssn_edit.text()
        user = self.username_edit.text()
        password = self.pass_edit.text()
        email = self.email_edit.text()
        if(self.maleRadio.isChecked()):
            gender = 'Male'
        elif(self.femaleRadio.isChecked()):
            gender = 'Female'
        elif(self.nonbinaryradio.isChecked()):
            gender = 'Non-Binary'
        else:
            gender = None
        mycursor = db.mycursor
        add_user = ("INSERT INTO stockmarket.users(fullname, ssn, username, pass, email, gender, balance) VALUES (%s, %s, %s, %s, %s, %s, %s)")
        data_user = (fullname, ssn, user, password, email, gender, 5000)
        try:
            mycursor.execute(add_user, data_user)
        except mysql.connector.Error as err:
            print("Something went wrong: {}".format(err))
            self.show_error()
        else:
            self.CurrentWindow.hide()
            self.LoginWindow.show()
            mydb.commit()

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    app.setWindowIcon(QtGui.QIcon("UI_Folder/icon.png"))
    app.setStyleSheet(qdarkstyle.load_stylesheet_pyqt5())
    CurrentWindow = QtWidgets.QMainWindow()
    ui = SignUpWindow()
    ui.setupUi(CurrentWindow, None)
    CurrentWindow.show()
    sys.exit(app.exec_())
