# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MemeLogin.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(437, 225)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(50, 70, 61, 16))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(50, 100, 55, 16))
        self.label_2.setObjectName("label_2")
        self.Username_lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.Username_lineEdit.setGeometry(QtCore.QRect(120, 70, 261, 22))
        self.Username_lineEdit.setObjectName("Username_lineEdit")
        self.password_LineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.password_LineEdit.setGeometry(QtCore.QRect(120, 100, 261, 22))
        self.password_LineEdit.setObjectName("password_LineEdit")
        self.Login_Button = QtWidgets.QPushButton(self.centralwidget)
        self.Login_Button.setGeometry(QtCore.QRect(230, 160, 93, 28))
        self.Login_Button.setObjectName("Login_Button")
        self.SignUp_Button = QtWidgets.QPushButton(self.centralwidget)
        self.SignUp_Button.setGeometry(QtCore.QRect(130, 160, 93, 28))
        self.SignUp_Button.setObjectName("SignUp_Button")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.SignUp_Button.clicked.connect(self.switch_sign)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Username "))
        self.label_2.setText(_translate("MainWindow", "Password"))
        self.Login_Button.setText(_translate("MainWindow", "Login"))
        self.SignUp_Button.setText(_translate("MainWindow", "SignUp"))
    
    def switch_sign(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = sign_window()
        self.ui.setupUi(self.window)
        MainWindow.hide()
        self.window.show()

class sign_window(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(474, 314)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(60, 60, 55, 16))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(60, 90, 55, 16))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(60, 120, 55, 16))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(60, 150, 55, 16))
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(60, 180, 55, 16))
        self.label_5.setObjectName("label_5")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(120, 60, 221, 22))
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_2.setGeometry(QtCore.QRect(120, 90, 221, 22))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.lineEdit_3 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_3.setGeometry(QtCore.QRect(120, 120, 221, 22))
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.lineEdit_4 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_4.setGeometry(QtCore.QRect(120, 150, 221, 22))
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.lineEdit_5 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_5.setGeometry(QtCore.QRect(120, 180, 221, 22))
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.Signup_button2 = QtWidgets.QPushButton(self.centralwidget)
        self.Signup_button2.setGeometry(QtCore.QRect(170, 240, 93, 28))
        self.Signup_button2.setObjectName("Signup_button2")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.Signup_button2.clicked.connect(self.Login_window)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("SignUp", "SignUp"))
        self.label.setText(_translate("MainWindow", "Fullname"))
        self.label_2.setText(_translate("MainWindow", "SSN"))
        self.label_3.setText(_translate("MainWindow", "Username"))
        self.label_4.setText(_translate("MainWindow", "Password"))
        self.label_5.setText(_translate("MainWindow", "Email"))
        self.Signup_button2.setText(_translate("MainWindow", "Donezo"))
    
    def Login_window(self):         
        MainWindow.close()
        MainWindow.show()


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
