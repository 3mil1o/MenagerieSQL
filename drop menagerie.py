import mysql.connector

connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password="1111"
)
cursor = connection.cursor()
cursor.execute("DROP DATABASE IF EXISTS menagerie")
print("Database 'menagerie' dropped (if it existed).")
connection.close()
