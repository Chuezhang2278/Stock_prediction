import sys, mysql.connector, icon_rc, qdarkstyle, datetime, DatabaseConnect as db
from PyQt5 import QtCore, QtGui, QtWidgets

# current user
ssn = ""
balance = 0
volume = 0
fullname = ""
selectedStock = ""
# stimulate login - to do, hard coding for now

# establish connection
connection = db.mydb
mycursor = db.mycursor

# initiate user information
def retrieveUserInfo():
    global fullname
    global balance
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

# gets number of volumn user owns for stock AAPL
def retrieveVolume():
    global volume
    mycursor.execute("SELECT volume FROM portfolio WHERE ssn = %s AND stockid = %s", (ssn, selectedStock))
    results = mycursor.fetchone()
    if results == None:
        mycursor.execute("INSERT INTO portfolio (ssn, stockid, volume) VALUES (%s, %s, 0)", (ssn, selectedStock))
        connection.commit()
        volume = 0
    else:
        volume = results[0]
    print("He owns " + str(volume) + " " + selectedStock + " stocks")

