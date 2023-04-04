import mysql.connector

connection = mysql.connector.connect(
    host = "localhost",
    user = 'root',
    password = "Binyaminarfi26+",
    database = "LaPlateforme"
)

cursor = connection.cursor()

cursor.execute('SELECT * FROM etudiant')
resultat = cursor.fetchall()

print(resultat)

cursor.close()
connection.close()