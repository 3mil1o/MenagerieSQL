import mysql.connector

# Connect to MySQL server
connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password="1111"
)
print("Connected to MySQL Server")
connection.close()
