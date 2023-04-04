import mysql.connector

class ZooManager:
    def __init__(self):
        self.bdd = mysql.connector.connect(
            host="localhost",
            user="root",
            password="Binyaminarfi26+",
            database="zoo"
        )

    # Ajouter un nouvel animal
    def ajouter_animal(self, nom, race, id_cage, date_naissance, pays_origine):
        cursor = self.bdd.cursor()
        query = "INSERT INTO animal (nom, race, id_cage, date_naissance, pays_origine) VALUES (%s, %s, %s, %s, %s)"
        values = (nom, race, id_cage, date_naissance, pays_origine)
        cursor.execute(query, values)
        self.bdd.commit()
        return cursor.lastrowid

    # Modifier les informations d'un animal existant
    def modifier_animal(self, id_animal, nom, race, id_cage, date_naissance, pays_origine):
        cursor = self.bdd.cursor()
        query = "UPDATE animal SET nom = %s, race = %s, id_cage = %s, date_naissance = %s, pays_origine = %s WHERE id_animal = %s"
        values = (nom, race, id_cage, date_naissance, pays_origine, id_animal)
        cursor.execute(query, values)
        self.bdd.commit()

    # Supprimer un animal existant
    def supprimer_animal(self, id_animal):
        cursor = self.bdd.cursor()
        query = "DELETE FROM animal WHERE id_animal = %s"
        values = (id_animal,)
        cursor.execute(query, values)
        self.bdd.commit()

    # Ajouter une nouvelle cage
    def ajouter_cage(self, superficie, capacite_max):
        cursor = self.bdd.cursor()
        query = "INSERT INTO cage (superficie, capacite_max) VALUES (%s, %s)"
        values = (superficie, capacite_max)
        cursor.execute(query, values)
        self.bdd.commit()
        return cursor.lastrowid

    # Modifier les informations d'une cage existante
    def modifier_cage(self, id_cage, superficie, capacite_max):
        cursor = self.bdd.cursor()
        query = "UPDATE cage SET superficie = %s, capacite_max = %s WHERE id_cage = %s"
        values = (superficie, capacite_max, id_cage)
        cursor.execute(query, values)
        self.bdd.commit()

    # Supprimer une cage existante
    def supprimer_cage(self, id_cage):
        cursor = self.bdd.cursor()
        query = "DELETE FROM cage WHERE id_cage = %s"
        values = (id_cage,)
        cursor.execute(query, values)
        self.bdd.commit()

    # Afficher la liste de tous les animaux
    def afficher_animaux(self):
        cursor = self.bdd.cursor(dictionary=True)
        query = "SELECT * FROM animal"
        cursor.execute(query)
        result = cursor.fetchall()
        for row in result:
            print(row)
    def calculer_superficie_totale(self):
        cursor = self.bdd.cursor()
        query = "SELECT SUM(superficie) FROM cage"
        cursor.execute(query)
        result = cursor.fetchone()
        superficie_totale = result[0]
        return superficie_totale

zoo_manager = ZooManager()


#Modifier les informations d'un animal existant
print(zoo_manager.calculer_superficie_totale())


zoo_manager.afficher_animaux()