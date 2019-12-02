import sys, mysql.connector, icon_rc, qdarkstyle, datetime, DatabaseConnect as db
from StockWindow import StockWindow
from PyQt5 import QtCore, QtGui, QtWidgets

# current user
ssn = ""
balance = 0
selectedStock = ""
volume = 0
fullname = ""

# stimulate login - to do, hard coding for now
ssn = "123456789"

# establish connection
connection = db.mydb
mycursor = db.mycursor

# initiate user information
mycursor.execute("SELECT fullname, balance FROM users WHERE ssn = %s", [ssn])
results = mycursor.fetchone()
if results != None:
    print("SSN found!")
    fullname = results[0]
    print("The full name of the person is " + fullname)
    balance = results[1]
    print("His balance is $" + str(balance))
else:
    print("No SSN like that found.")

# stimulate user stock selection
selectedStock = "AAPL"

# gets number of volumn user owns for stock AAPL
mycursor.execute("SELECT volume FROM portfolio WHERE ssn = %s AND stockid = %s", (ssn, selectedStock))
results = mycursor.fetchone()
if results == None:
    volume = 0
else:
    volume = results[0]
print("He owns " + str(volume) + " " + selectedStock + " stocks")

# stimulate buying/selling stock - need to change this later to connect to some other window
app = QtWidgets.QApplication(sys.argv)
app.setWindowIcon(QtGui.QIcon("UI_Folder/icon.png"))
app.setStyleSheet(qdarkstyle.load_stylesheet_pyqt5())
Window = QtWidgets.QMainWindow()
ui = StockWindow(selectedStock, volume, ssn)
ui.setupUi(Window)
Window.show()
sys.exit(app.exec_())
