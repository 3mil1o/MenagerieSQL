import mysql.connector

connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password="1111"
)
cursor = connection.cursor()
cursor.execute("SHOW DATABASES")
for db in cursor:
    print(db)
connection.close()
