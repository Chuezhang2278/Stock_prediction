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

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Username "))
        self.label_2.setText(_translate("MainWindow", "Password"))
        self.Login_Button.setText(_translate("MainWindow", "Login"))
        self.SignUp_Button.setText(_translate("MainWindow", "SignUp"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
