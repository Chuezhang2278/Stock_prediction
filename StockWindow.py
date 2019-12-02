# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'StockData.ui',
# licensing of 'StockData.ui' applies.
#
# Created: Wed Nov 20 20:59:50 2019
#      by: pyside2-uic  running on PySide2 5.13.2
#
# WARNING! All changes made in this file will be lost!

import sys, icon_rc, qdarkstyle, datetime, mysql.connector, DatabaseConnect as db
import pandas as pd
import matplotlib.pyplot as plt
import pyqtgraph as pg

from PyQt5 import QtCore, QtGui, QtWidgets
from pandas_datareader import data as data, wb

class StockWindow(object):
    def __init__(self, name, shares, ssn):
        self.stock_name = name
        self.shares = shares
        self.df = None
        self.ssn = ssn

    def setupUi(self, CurrentWindow):
        self.CurrentWindow = CurrentWindow
        CurrentWindow.setObjectName("CurrentWindow")
        CurrentWindow.resize(1097, 1145)
        CurrentWindow.setStyleSheet("")
        self.seven_days = QtWidgets.QPushButton(CurrentWindow)
        self.seven_days.setGeometry(QtCore.QRect(40, 590, 111, 51))
        self.seven_days.setObjectName("seven_days")
        self.icon = QtWidgets.QLabel(CurrentWindow)
        self.icon.setGeometry(QtCore.QRect(1030, 0, 71, 71))
        self.icon.setText("")
        self.icon.setPixmap(QtGui.QPixmap(":/newPrefix/icon.png"))
        self.icon.setObjectName("icon")
        self.two_weeks = QtWidgets.QPushButton(CurrentWindow)
        self.two_weeks.setGeometry(QtCore.QRect(190, 590, 111, 51))
        self.two_weeks.setObjectName("two_weeks")
        self.one_month = QtWidgets.QPushButton(CurrentWindow)
        self.one_month.setGeometry(QtCore.QRect(340, 590, 111, 51))
        self.one_month.setObjectName("one_month")
        self.six_months = QtWidgets.QPushButton(CurrentWindow)
        self.six_months.setGeometry(QtCore.QRect(640, 590, 111, 51))
        self.six_months.setObjectName("six_months")
        self.three_months = QtWidgets.QPushButton(CurrentWindow)
        self.three_months.setGeometry(QtCore.QRect(490, 590, 111, 51))
        self.three_months.setObjectName("three_months")
        self.one_year = QtWidgets.QPushButton(CurrentWindow)
        self.one_year.setGeometry(QtCore.QRect(790, 590, 111, 51))
        self.one_year.setObjectName("one_year")
        self.three_year = QtWidgets.QPushButton(CurrentWindow)
        self.three_year.setGeometry(QtCore.QRect(940, 590, 111, 51))
        self.three_year.setObjectName("three_year")
        self.stock_name_label = QtWidgets.QLabel(CurrentWindow)
        self.stock_name_label.setGeometry(QtCore.QRect(40, 670, 1031, 81))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setWeight(75)
        font.setBold(True)
        self.stock_name_label.setFont(font)
        self.stock_name_label.setStyleSheet("background-color: #2a373f;")
        self.stock_name_label.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.stock_name_label.setObjectName("stock_name_label")
        self.high_label = QtWidgets.QLabel(CurrentWindow)
        self.high_label.setGeometry(QtCore.QRect(40, 840, 490, 51))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.high_label.setFont(font)
        self.high_label.setStyleSheet("background-color: #445661; border-radius: 5px;")
        self.high_label.setObjectName("high_label")
        self.low_label = QtWidgets.QLabel(CurrentWindow)
        self.low_label.setGeometry(QtCore.QRect(40, 910, 490, 51))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.low_label.setFont(font)
        self.low_label.setStyleSheet("background-color: #445661; border-radius: 5px;")
        self.low_label.setObjectName("low_label")
        self.open_label = QtWidgets.QLabel(CurrentWindow)
        self.open_label.setGeometry(QtCore.QRect(580, 840, 490, 51))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.open_label.setFont(font)
        self.open_label.setStyleSheet("background-color: #445661; border-radius: 5px;")
        self.open_label.setObjectName("open_label")
        self.close_label = QtWidgets.QLabel(CurrentWindow)
        self.close_label.setGeometry(QtCore.QRect(580, 910, 490, 51))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.close_label.setFont(font)
        self.close_label.setStyleSheet("background-color: #445661; border-radius: 5px;")
        self.close_label.setObjectName("close_label")
        self.volumes_trade_label = QtWidgets.QLabel(CurrentWindow)
        self.volumes_trade_label.setGeometry(QtCore.QRect(580, 770, 490, 51))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.volumes_trade_label.setFont(font)
        self.volumes_trade_label.setStyleSheet("background-color: #445661; border-radius: 5px;")
        self.volumes_trade_label.setObjectName("volumes_trade_label")
        self.change_label = QtWidgets.QLabel(CurrentWindow)
        self.change_label.setGeometry(QtCore.QRect(40, 770, 490, 51))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.change_label.setFont(font)
        self.change_label.setStyleSheet("background-color: #445661; border-radius: 5px;")
        self.change_label.setObjectName("change_label")
        self.buy_edit = QtWidgets.QLineEdit(CurrentWindow)
        self.buy_edit.setGeometry(QtCore.QRect(150, 985, 131, 31))
        self.buy_edit.setText("0")
        self.buy_edit.setObjectName("buy_edit")
        self.buy_edit.setValidator(QtGui.QIntValidator())
        self.back_button = QtWidgets.QPushButton(CurrentWindow)
        self.back_button.setGeometry(QtCore.QRect(40, 20, 111, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.back_button.setFont(font)
        self.back_button.setObjectName("back_button")
        self.back_button.clicked.connect(self.return_to_parent)
        self.buy_button = QtWidgets.QPushButton(CurrentWindow)
        self.buy_button.setGeometry(QtCore.QRect(300, 985, 101, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.buy_button.setFont(font)
        self.buy_button.setObjectName("buy_button")
        self.sell_button = QtWidgets.QPushButton(CurrentWindow)
        self.sell_button.setGeometry(QtCore.QRect(850, 985, 101, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.sell_button.setFont(font)
        self.sell_button.setObjectName("sell_button")
        self.sell_edit = QtWidgets.QLineEdit(CurrentWindow)
        self.sell_edit.setGeometry(QtCore.QRect(700, 985, 131, 31))
        self.sell_edit.setText("0")
        self.sell_edit.setObjectName("sell_edit")
        self.sell_edit.setValidator(QtGui.QIntValidator())
        self.background_label = QtWidgets.QLabel(CurrentWindow)
        self.background_label.setGeometry(QtCore.QRect(30, 660, 1051, 471))
        self.background_label.setStyleSheet("background-color: #2a373f; border-radius: 5px;")
        self.background_label.setText("")
        self.background_label.setIndent(-1)
        self.background_label.setObjectName("label")
        self.background_label.lower()
        self.graphicsView = pg.PlotWidget(CurrentWindow)
        self.graphicsView.setGeometry(QtCore.QRect(40, 75, 1025, 500))

        self.seven_days.clicked.connect(self.seven_days_clicked)
        self.two_weeks.clicked.connect(self.two_weeks_clicked)
        self.one_month.clicked.connect(self.one_month_clicked)
        self.three_months.clicked.connect(self.three_months_clicked)
        self.six_months.clicked.connect(self.six_months_clicked)
        self.one_year.clicked.connect(self.one_year_clicked)
        self.three_year.clicked.connect(self.three_year_clicked)
        self.sell_button.clicked.connect(self.sell_stock)
        self.buy_button.clicked.connect(self.buy_stock)

        self.retranslateUi(CurrentWindow)
        QtCore.QMetaObject.connectSlotsByName(CurrentWindow)

    def retranslateUi(self, CurrentWindow):
        CurrentWindow.setWindowTitle(QtWidgets.QApplication.translate("CurrentWindow", "Stock Info", None, -1))
        self.seven_days.setText(QtWidgets.QApplication.translate("CurrentWindow", "7 Days", None, -1))
        self.two_weeks.setText(QtWidgets.QApplication.translate("CurrentWindow", "2 Weeks", None, -1))
        self.one_month.setText(QtWidgets.QApplication.translate("CurrentWindow", "1 Month", None, -1))
        self.six_months.setText(QtWidgets.QApplication.translate("CurrentWindow", "6 Months", None, -1))
        self.three_months.setText(QtWidgets.QApplication.translate("CurrentWindow", "3 Months", None, -1))
        self.one_year.setText(QtWidgets.QApplication.translate("CurrentWindow", "1 Year", None, -1))
        self.three_year.setText(QtWidgets.QApplication.translate("CurrentWindow", "3 Years", None, -1))
        self.stock_name_label.setText(QtWidgets.QApplication.translate("CurrentWindow", "Stock Name Today (5 Shares)", None, -1))
        self.high_label.setText(QtWidgets.QApplication.translate("CurrentWindow", "Today's High Share Value:", None, -1))
        self.low_label.setText(QtWidgets.QApplication.translate("CurrentWindow", "Today's Low Share Value:", None, -1))
        self.open_label.setText(QtWidgets.QApplication.translate("CurrentWindow", "Today's Open Share Value:", None, -1))
        self.close_label.setText(QtWidgets.QApplication.translate("CurrentWindow", "Today's Close Share Value:", None, -1))
        self.volumes_trade_label.setText(QtWidgets.QApplication.translate("CurrentWindow", "Volumes Traded Today:", None, -1))
        self.change_label.setText(QtWidgets.QApplication.translate("CurrentWindow", "% CHANGE, +- $$", None, -1))
        self.back_button.setText(QtWidgets.QApplication.translate("CurrentWindow", "Back", None, -1))
        self.buy_button.setText(QtWidgets.QApplication.translate("CurrentWindow", "Buy", None, -1))
        self.sell_button.setText(QtWidgets.QApplication.translate("CurrentWindow", "Sell", None, -1))
        self.plot(self.stock_name, 365)
        self.stock_name_label_update()
        self.volumes_trade_label_update()
        self.high_label_update()
        self.low_label_update()
        self.open_label_update()
        self.close_label_update()

    def declare_stock_name(self, name):
        self.stock_name = name

    def plot(self, name, offset):
        '''
        name is the codename of the stock to be retrieved
        offset is the day offset from when you want to show the data (365 = from now to 1 year ago)
        '''
        end = datetime.datetime.today()
        start = end + datetime.timedelta(days=-offset)
        df = data.DataReader(name, 'yahoo', start, end)
        self.df = df
        df.index=pd.to_datetime(df.index)
        self.graphicsView.clear()
        self.graphicsView.setTitle(name + " Stocks: from " + start.strftime('%m/%d/%Y') + " to " + end.strftime('%m/%d/%Y'))
        self.graphicsView.setLabel("left", text="High (USD)")
        self.graphicsView.setLabel("bottom", text="Dates")
        self.graphicsView.plot(df['High'])
        self.change_label_update(start, end)

    def buy_stock(self):
        value = self.df["High"].tail()[-1]
        num = int(self.buy_edit.text())
        db.mycursor.execute("SELECT balance FROM users WHERE ssn = %s", [self.ssn])
        results = db.mycursor.fetchone()
        curr_balance = results[0]
        if num < 1:
            print("User must enter a positive integer.")
        elif num * value > curr_balance:
            print("User does not have " + str(num * value) + " dollars to buy " + num + " stocks.")
        else:
            print("User bought " + str(num) + " shares!")
            print("Subtracted " + str(value * num) + " to the User's balance!")
            self.shares += num
            db.mycursor.execute("UPDATE portfolio SET volume = %s WHERE ssn = %s AND stockid = %s", (self.shares, self.ssn, self.stock_name))
            new_balance = curr_balance - (value * num)
            print("New balance is " + str(new_balance) + ".")
            db.mycursor.execute("UPDATE users SET balance = %s WHERE ssn = %s", (float(new_balance), self.ssn))
            db.mydb.commit()
            self.stock_name_label_update()

    def sell_stock(self):
        value = self.df["High"].tail()[-1]
        num = int(self.sell_edit.text())
        if num < 1:
            print("User must enter a positive integer.")
        elif num > self.shares:
            print("User does not have " + str(num) + " stocks to sell.")
        else:
            print("User sold " + str(num) + " shares!")
            print("Added " + str(value * num) + " to the User's balance!")
            self.shares -= num
            # update number of volume
            db.mycursor.execute("UPDATE portfolio SET volume = %s WHERE ssn = %s AND stockid = %s", (self.shares, self.ssn, self.stock_name))
            # find current balance
            db.mycursor.execute("SELECT balance FROM users WHERE ssn = %s", [self.ssn])
            results = db.mycursor.fetchone()
            new_balance = results[0] + (value * num)
            print("New balance is " + str(new_balance) + ".")
            # update new balance
            db.mycursor.execute("UPDATE users SET balance = %s WHERE ssn = %s", (float(new_balance), self.ssn))
            db.mydb.commit()
            self.stock_name_label_update()

    def stock_name_label_update(self):
        self.stock_name_label.setText(str(self.stock_name) + " Share Prices (You own " + str(self.shares) +" shares)")

    def change_label_update(self, start, end):
        start_value = self.df["High"].head(1)[0]
        end_value = self.df["High"].tail(1)[-1]
        if(end_value > start_value):
            self.change_label.setText("Changes since " + start.strftime('%m/%d/%Y') + " to " + end.strftime('%m/%d/%Y') + ": +" + str(self.calculate_change(start_value, end_value)) + "%")
        else:
            self.change_label.setText("Changes since " + start.strftime('%m/%d/%Y') + " to " + end.strftime('%m/%d/%Y') + ": -" + str(self.calculate_change(start_value, end_value)) + "%")

    def volumes_trade_label_update(self):
        self.volumes_trade_label.setText("Shares Traded Today: " + str(self.df["Volume"].tail()[-1]))

    def high_label_update(self):
        self.high_label.setText("Today's High Share Value: $" + str(self.df["High"].tail()[-1]))

    def low_label_update(self):
        self.low_label.setText("Today's Low Share Value: $" + str(self.df["Low"].tail()[-1]))

    def open_label_update(self):
        self.open_label.setText("Today's Open Share Value: $" + str(self.df["Open"].tail()[-1]))

    def close_label_update(self):
        self.close_label.setText("Today's Close Share Value: $" + str(self.df["Close"].tail()[-1]))

    def seven_days_clicked(self):
        self.plot(self.stock_name, 7)

    def two_weeks_clicked(self):
        self.plot(self.stock_name, 14)

    def one_month_clicked(self):
        self.plot(self.stock_name, 30)

    def three_months_clicked(self):
        self.plot(self.stock_name, 90)

    def six_months_clicked(self):
        self.plot(self.stock_name, 180)

    def one_year_clicked(self):
        self.plot(self.stock_name, 365)

    def three_year_clicked(self):
        self.plot(self.stock_name, 1095)

    def connectWindows(self, ParentWindow):
        self.ParentWindow = ParentWindow

    def return_to_parent(self):
        self.CurrentWindow.hide()
        self.ParentWindow.show()

    def calculate_change(self, start, end):
        if start == end:
            return 0
        diff = end - start
        percent = (diff / end) * 100
        return round(percent, 2)

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    app.setWindowIcon(QtGui.QIcon("UI_Folder/icon.png"))
    app.setStyleSheet(qdarkstyle.load_stylesheet_pyqt5())
    CurrentWindow = QtWidgets.QMainWindow()
    ui = StockWindow("AAPL", 99, '123456789')
    ui.setupUi(CurrentWindow)
    CurrentWindow.show()
    sys.exit(app.exec_())
