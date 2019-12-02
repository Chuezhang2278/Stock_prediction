import mysql.connector

mydb = mysql.connector.connect(
    host='localhost',
    user='root',
    password='123password',
    database='stockmarket')

mycursor = mydb.cursor(buffered=True)


# try:
#     pass
# except Exception:
#     import traceback
#     print(traceback.format_exc())
