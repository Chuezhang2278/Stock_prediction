import mysql.connector

## FILE MADE FOR TESTING OUT DATABASE ##


mydb = mysql.connector.connect(
    host='localhost',
    user='root',
    password='123password',
    database='MemeStock'
)

mycursor = mydb.cursor()
#sql = "DELETE FROM users WHERE pass = 'b'"
#mycursor.execute(sql)
############################### MAKING DATABASE, INSERTING INTO DB ###################

#mycursor.execute("CREATE DATABASE MemeStock")
#mycursor.execute("CREATE TABLE users (Fullname VARCHAR(255), SSN INTEGER(9), Username VARCHAR(255), Pass VARCHAR(15), Email VARCHAR(255))")
sqlFormula = "INSERT INTO users (Fullname, SSN, Username, Pass, Email) VALUES (%s, %s, %s, %s, %s)"
bob = [("Cook", "987654321", "John", "1", "cook@gmail.com"),
      ("a", "123456789", "a", "b", "RealJohnDoe@gmail.com")]

mycursor.executemany(sqlFormula, bob)
mydb.commit()

######################################################################################
