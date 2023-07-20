import pyodbc

conn = "DRIVER={SQL SERVER};SERVER=localhost;DATABASE=dbTest;TRUSTED_CONNECTION=yes;"
connection = pyodbc.connect(conn)
cursor = connection.cursor()

cursor.execute("SELECT * FROM Person")
for item in cursor:
    print(item)