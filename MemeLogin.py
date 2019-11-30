import sys, icon_rc, qdarkstyle, mysql.connector
from PyQt5 import QtCore, QtGui, QtWidgets
from MainWindow import MemeWindow
from SignUp import SignUpWindow

class LoginWindow(object):
    def setupUi(self, CurrentWindow):
        CurrentWindow.setObjectName("CurrentWindow")
        CurrentWindow.setEnabled(True)
        CurrentWindow.resize(461, 253)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(CurrentWindow.sizePolicy().hasHeightForWidth())
        CurrentWindow.setSizePolicy(sizePolicy)
        CurrentWindow.setMinimumSize(QtCore.QSize(461, 253))
        CurrentWindow.setMaximumSize(QtCore.QSize(461, 253))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/newPrefix/icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        CurrentWindow.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(CurrentWindow)
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
        CurrentWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(CurrentWindow)
        self.statusbar.setObjectName("statusbar")
        CurrentWindow.setStatusBar(self.statusbar)

        self.retranslateUi(CurrentWindow)
        QtCore.QMetaObject.connectSlotsByName(CurrentWindow)

        self.signup_button.clicked.connect(self.signup)
        self.login_button.clicked.connect(self.login)

    def retranslateUi(self, CurrentWindow):
        CurrentWindow.setWindowTitle(QtWidgets.QApplication.translate("CurrentWindow", "Log In", None, -1))
        self.username_label.setText(QtWidgets.QApplication.translate("CurrentWindow", "Username:", None, -1))
        self.password_label.setText(QtWidgets.QApplication.translate("CurrentWindow", "Password:", None, -1))
        self.login_button.setText(QtWidgets.QApplication.translate("CurrentWindow", "Login", None, -1))
        self.signup_button.setText(QtWidgets.QApplication.translate("CurrentWindow", "Sign Up", None, -1))

    def signup(self):
        print("called1")
        self.SignUpWindow = QtWidgets.QMainWindow()
        self.ui = SignUpWindow()
        self.ui.setupUi(self.SignUpWindow, CurrentWindow)
        print("called")
        self.SignUpWindow.show()
        CurrentWindow.hide()

    def login(self):
        username_text = self.username_edit.text()
        password_text = self.password_edit.text()

        mydb = mysql.connector.connect(
            host='localhost',
            user='root',
            password='123password',
            database='memestock')

        mycursor = mydb.cursor()

        mycursor.execute("SELECT username, pass FROM users WHERE username = %s AND pass = %s", (username_text, password_text))
        usercheck = mycursor.fetchone()
        if(usercheck != None and usercheck[0] == username_text and usercheck[1] == password_text):
            print("Login Success!")
            self.MemeWindow = QtWidgets.QMainWindow()
            self.ui = MemeWindow()
            self.ui.setupUi(self.MemeWindow)
            CurrentWindow.hide()
            self.MemeWindow.show()
        else:
            print("Login Failed!")


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    app.setWindowIcon(QtGui.QIcon("UI_Folder/icon.png"))
    app.setStyleSheet(qdarkstyle.load_stylesheet_pyqt5())
    CurrentWindow = QtWidgets.QMainWindow()
    ui = LoginWindow()
    ui.setupUi(CurrentWindow)
    CurrentWindow.show()
    sys.exit(app.exec_())
