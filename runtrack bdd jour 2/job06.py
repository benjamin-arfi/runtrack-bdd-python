import mysql.connector

connection = mysql.connector.connect(
    host = "localhost",
    user = 'root',
    password = "Binyaminarfi26+",
    database = "LaPlateforme"
)

cursor = connection.cursor()

cursor.execute(' SELECT CONCAT("La capacite de toutes les salles est de : ", sum(capacite) ) FROM salles')
resultat = cursor.fetchall()
print(resultat)

cursor.close()
connection.close()