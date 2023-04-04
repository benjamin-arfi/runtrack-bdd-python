import mysql.connector

connection = mysql.connector.connect(
    host = "localhost",
    user = 'root',
    password = "Binyaminarfi26+",
    database = "LaPlateforme"
)

cursor = connection.cursor()

cursor.execute('SELECT CONCAT("La superficie de La Plateforme est de ", SUM(superficie), " m2") as X FROM etage;')
resultat = cursor.fetchall()
print(resultat)

cursor.close()
connection.close()