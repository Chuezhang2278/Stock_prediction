import mysql.connector

mydb = mysql.connector.connect(
    host='localhost',
    user='root',
    password='123password',
    database='testdb'
)

mycursor = mydb.cursor()

#mycursor.execute("CREATE DATABASE testdb")
#mycursor.execute("CREATE TABLE users (Fullname VARCHAR(255), Email VARCHAR(255))")
mycursor.execute("SHOW TABLES")

for db in mycursor:
    print(db)