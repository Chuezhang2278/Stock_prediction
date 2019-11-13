# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'SignUp.ui',
# licensing of 'SignUp.ui' applies.
#
# Created: Thu Nov  7 23:03:41 2019
#      by: pyside2-uic  running on PySide2 5.13.2
#
# WARNING! All changes made in this file will be lost!
import sys, icon_rc, qdarkstyle, mysql.connector
from PySide2 import QtCore, QtGui, QtWidgets

class SignUpWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(446, 306)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QtCore.QSize(446, 306))
        MainWindow.setMaximumSize(QtCore.QSize(446, 306))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/newPrefix/icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(60, 60, 71, 16))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(60, 90, 55, 16))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(60, 120, 71, 16))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(60, 150, 71, 16))
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(60, 180, 61, 16))
        self.label_5.setObjectName("label_5")
        self.Name_lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.Name_lineEdit.setGeometry(QtCore.QRect(140, 60, 221, 22))
        self.Name_lineEdit.setObjectName("Name_lineEdit")
        self.SSN_lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.SSN_lineEdit.setGeometry(QtCore.QRect(140, 90, 221, 22))
        self.SSN_lineEdit.setObjectName("SSN_lineEdit")
        self.User_lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.User_lineEdit.setGeometry(QtCore.QRect(140, 120, 221, 22))
        self.User_lineEdit.setObjectName("User_lineEdit")
        self.PW_lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.PW_lineEdit.setGeometry(QtCore.QRect(140, 150, 221, 22))
        self.PW_lineEdit.setObjectName("PW_lineEdit")
        self.Email_lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.Email_lineEdit.setGeometry(QtCore.QRect(140, 180, 221, 22))
        self.Email_lineEdit.setObjectName("Email_lineEdit")
        self.Signup_button2 = QtWidgets.QPushButton(self.centralwidget)
        self.Signup_button2.setGeometry(QtCore.QRect(180, 240, 93, 28))
        self.Signup_button2.setObjectName("Signup_button2")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(60, 210, 61, 16))
        self.label_6.setObjectName("label_6")
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
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.Signup_button2.clicked.connect(self.add_user)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtWidgets.QApplication.translate("MainWindow", "Sign Up - Meme Stock Market", None, -1))
        self.label.setText(QtWidgets.QApplication.translate("MainWindow", "Full Name:", None, -1))
        self.label_2.setText(QtWidgets.QApplication.translate("MainWindow", "SSN:", None, -1))
        self.label_3.setText(QtWidgets.QApplication.translate("MainWindow", "Username:", None, -1))
        self.label_4.setText(QtWidgets.QApplication.translate("MainWindow", "Password:", None, -1))
        self.label_5.setText(QtWidgets.QApplication.translate("MainWindow", "Email:", None, -1))
        self.Signup_button2.setText(QtWidgets.QApplication.translate("MainWindow", "Finish", None, -1))
        self.label_6.setText(QtWidgets.QApplication.translate("MainWindow", "Gender:", None, -1))
        self.maleRadio.setText(QtWidgets.QApplication.translate("MainWindow", "Male", None, -1))
        self.femaleRadio.setText(QtWidgets.QApplication.translate("MainWindow", "Female", None, -1))
        self.nonbinaryradio.setText(QtWidgets.QApplication.translate("MainWindow", "Non-Binary", None, -1))
    
    def add_user(self):
        mydb = mysql.connector.connect(
            host='localhost',
            user='root',
            password='123password',
            database='memestock')
        
        Fullname = self.Name_lineEdit.text()
        SSN = self.SSN_lineEdit.text()
        User = self.User_lineEdit.text()
        Password = self.PW_lineEdit.text()
        E = self.Email_lineEdit.text()

        mycursor = mydb.cursor()

        add_user = ("INSERT INTO memestock.users(Fullname, SSN, Username, Pass, Email) VALUES (%s, %s, %s, %s, %s)")

        data_user = (Fullname, SSN, User, Password, E)

        mycursor.execute(add_user, data_user)

        mydb.commit()

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    app.setWindowIcon(QtGui.QIcon("UI_Folder/icon.png"))
    MainWindow = QtWidgets.QMainWindow()
    ui = SignUpWindow()
    ui.setupUi(MainWindow)
    app.setStyleSheet(qdarkstyle.load_stylesheet_pyqt5())
    MainWindow.show()
    sys.exit(app.exec_())
