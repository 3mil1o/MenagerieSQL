import mysql.connector

connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password="1111"
)
cursor = connection.cursor()
cursor.execute("CREATE DATABASE menagerie")
print("Database 'menagerie' created.")
connection.close()
