import mysql.connector

connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password="1111",
    database="menagerie"
)

cursor = connection.cursor()

query = "SELECT * FROM pet WHERE species = 'dog' AND sex = 'f'"
cursor.execute(query)

results = cursor.fetchall()

if results:
    print("Results:")
    for record in results:
        name, owner, species, sex, birth, death = record
        print(f"Name: {name}, Owner: {owner}, Species: {species}, Sex: {sex}, Birth: {birth}, Death: {death if death else 'N/A'}")
else:
    print("No records found.")

connection.close()
