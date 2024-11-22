import mysql.connector

connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password="1111",
    database="menagerie"
)
cursor = connection.cursor()
cursor.execute("SELECT name, birth FROM pet")
for record in cursor:
    print(record)
connection.close()
