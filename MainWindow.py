# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'CurrentWindow.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!

import sys, icon_rc, qdarkstyle, datetime, mysql.connector, DatabaseConnect as db, UserInfo
from PyQt5 import QtCore, QtGui, QtWidgets
from StockWindow import StockWindow
from pandas_datareader import data as data, wb

class MemeWindow(object):
    def setupUi(self, CurrentWindow):
        self.CurrentWindow = CurrentWindow
        CurrentWindow.setObjectName("CurrentWindow")
        CurrentWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(CurrentWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(20, 30, 760, 540))
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.tabWidget.addTab(self.tab_2, "")
        self.label = QtWidgets.QLabel(self.tab_2)
        self.label.setGeometry(QtCore.QRect(0, 0, 191, 61))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.tab_2)
        self.label_2.setGeometry(QtCore.QRect(200, 20, 71, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.trans_listView = QtWidgets.QListWidget(self.tab_2)
        self.trans_listView.setGeometry(QtCore.QRect(35, 90, 321, 380))
        self.trans_listView.setStyleSheet("")
        self.trans_listView.setFrameShape(QtWidgets.QFrame.HLine)
        self.trans_listView.setObjectName("Transaction List")
        

        connection = db.mydb
        mycursor = db.mycursor
        sql = "SELECT trades.TradeID, trades.StockID, trades.PricePerShare, trades.Volume, trades.Date, trades.TotalCost FROM trades WHERE trades.SSN = %s"
        mycursor.execute(sql, [UserInfo.ssn])
        transaction = mycursor.fetchall()
        print(transaction[0][0])
        for x in transaction:
            self.trans_listView.addItem(str(x))

        # sqlJoin = "SELECT \
        #     users.Fullname, users.Balance AS user, \
        #     portfolio.StockID, portfolio.Volume AS stock \
        #     FROM users \
        #     JOIN portfolio ON users.SSN = portfolio.SSN \
        #     WHERE users.SSN = %s"
        # sqlJoin2 = "SELECT \
        #     users.Fullname, users.Balance AS user, \
        #     trades.Volume, trades.PricePerShare, trades.TotalCost, trades.Date AS trade \
        #     FROM users \
        #     JOIN trades ON users.SSN = trades.SSN \
        #     WHERE users.SSN = %s"
        # mycursor.execute(sqlJoin2, [UserInfo.ssn])
        # myresult = mycursor.fetchall()
        # #transaction = myresult[0]
        # #self.trans_listView.addItem(str(transaction))

        # mycursor.execute(sqlJoin, [UserInfo.ssn])
        # results = mycursor.fetchall()
        # print(mycursor.rowcount)
        # if results != None:
        #     balance = results[0]
        
        self.holding_listView_2 = QtWidgets.QListWidget(self.tab_2)
        self.holding_listView_2.setGeometry(QtCore.QRect(400, 90, 321, 380))
        self.holding_listView_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.holding_listView_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.holding_listView_2.setObjectName("Holding List")
        # self.holding_listView_2.addItem(str(balance))
        self.label_4 = QtWidgets.QLabel(self.tab_2)
        self.label_4.setGeometry(QtCore.QRect(400, 60, 131, 21))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(11)
        font.setBold(True)
        font.setUnderline(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.label_3 = QtWidgets.QLabel(self.tab_2)
        self.label_3.setGeometry(QtCore.QRect(35, 60, 201, 21))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(11)
        font.setBold(True)
        font.setUnderline(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.tabWidget.addTab(self.tab_2, "")
        CurrentWindow.setCentralWidget(self.centralwidget)

        #TEST STUFF
        self.stock_button = QtWidgets.QPushButton(self.tab)
        self.stock_button.setGeometry(QtCore.QRect(320, 160, 93, 28))
        self.stock_button.setObjectName("stock_button")
        self.stock_button.clicked.connect(self.stock_click)
        self.stock_edit = QtWidgets.QLineEdit(self.tab)
        self.stock_edit.setGeometry(QtCore.QRect(300, 200, 131, 31))
        self.stock_edit.setText("")
        self.stock_edit.setObjectName("stock_edit")
        self.high_label = QtWidgets.QLabel(self.tab)
        self.high_label.setGeometry(QtCore.QRect(245, 250, 250, 150))
        self.high_label.setStyleSheet("background-color: #445661; border-radius: 5px;")
        self.high_label.setObjectName("high_label")
        self.high_label.setText("Hey cutie, please enter a legit stock ID :)\nYou can use anything you want\nHere are some examples: \n'AMZN' for Amazon \n'M' for Macys \n'AAPL' for Apple \n'AMD' for AMD \n'INTC' for Intel")
        #TEST STUFF
        self.retranslateUi(CurrentWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(CurrentWindow)

    def retranslateUi(self, CurrentWindow):
        _translate = QtCore.QCoreApplication.translate
        CurrentWindow.setWindowTitle(_translate("CurrentWindow", "Main Window"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "Stocks"))
        self.stock_button.setText(QtWidgets.QApplication.translate("CurrentWindow", "Stock", None, -1))
        self.label.setText(_translate("MainWindow", "Total Value:"))
        self.label_2.setText(_translate("MainWindow", "MONI"))
        self.label_4.setText(_translate("MainWindow", "Holdings"))
        self.label_3.setText(_translate("MainWindow", "Transaction History"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "Profile Page"))

    def stock_click(self):
        try:
            data.DataReader(self.stock_edit.text(), 'yahoo')
        except:
            self.high_label.setText("Enter a legit company stock ID >.<")
        else:
            self.StockWindow = QtWidgets.QMainWindow()
            UserInfo.selectedStock = self.stock_edit.text()
            UserInfo.retrieveVolume()
            self.ui = StockWindow(self.stock_edit.text())
            self.ui.connectWindows(self.CurrentWindow)
            self.ui.setupUi(self.StockWindow)
            self.StockWindow.show()
            self.CurrentWindow.hide()
            self.high_label.setText("Hey cutie, please enter a legit stock ID :)  \n'AMZN' for Amazon \n'M' for Macys \n'AAPL' for Apple \n'AMD' for AMD \n'INTC' for Intel")

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    app.setWindowIcon(QtGui.QIcon("UI_Folder/icon.png"))
    app.setStyleSheet(qdarkstyle.load_stylesheet_pyqt5())
    CurrentWindow = QtWidgets.QMainWindow()
    ui = MemeWindow()
    ui.setupUi(CurrentWindow)
    CurrentWindow.show()
    sys.exit(app.exec_())
