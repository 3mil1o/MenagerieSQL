import mysql.connector

connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password="1111",
    database="menagerie"
)
cursor = connection.cursor()
cursor.execute("DESCRIBE pet")
for row in cursor:
    print(row)
connection.close()
