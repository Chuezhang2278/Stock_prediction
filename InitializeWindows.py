from MemeLogin import LoginWindow
import sys, icon_rc, qdarkstyle, mysql.connector
from PyQt5 import QtCore, QtGui, QtWidgets
from MainWindow import MemeWindow
from SignUp import SignUpWindow

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    app.setWindowIcon(QtGui.QIcon("UI_Folder/icon.png"))
    app.setStyleSheet(qdarkstyle.load_stylesheet_pyqt5())
    CurrentWindow = QtWidgets.QMainWindow()
    ui = LoginWindow()
    ui.setupUi(CurrentWindow)
    CurrentWindow.show()
    sys.exit(app.exec_())