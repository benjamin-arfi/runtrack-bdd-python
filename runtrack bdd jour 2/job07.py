import mysql.connector

class EmployesManager:
    def __init__(self):
        self.bdd = mysql.connector.connect(
            host="localhost",
            user="root",
            password="Binyaminarfi26+",
            database="laplateforme"
        )

    # Créer un nouvel employé
    def create(self, nom, prenom, salaire, id_service):
        cursor = self.bdd.cursor()
        query = "INSERT INTO employes (nom, prenom, salaire, id_service) VALUES (%s, %s, %s, %s)"
        values = (nom, prenom, salaire, id_service)
        cursor.execute(query, values)
        self.bdd.commit()
        return cursor.lastrowid

    # Lire un employé existant
    def read(self, id):
        cursor = self.bdd.cursor()
        query = "SELECT * FROM employes WHERE id = %s"
        values = (id,)
        cursor.execute(query, values)
        return cursor.fetchone()

    # Mettre à jour un employé existant
    def update(self, id, nom, prenom, salaire, id_service):
        cursor = self.bdd.cursor()
        query = "UPDATE employes SET nom = %s, prenom = %s, salaire = %s, id_service = %s WHERE id = %s"
        values = (nom, prenom, salaire, id_service, id)
        cursor.execute(query, values)
        self.bdd.commit()

    # Supprimer un employé existant
    def delete(self, id):
        cursor = self.bdd.cursor()
        query = "DELETE FROM employes WHERE id = %s"
        values = (id,)
        cursor.execute(query, values)
        self.bdd.commit()
employes_manager = EmployesManager()

 # Créer un nouvel employé
employes_manager.create("moi", "pate", 10000, 3)
print(employes_manager.read(25))

# Lire un employé existant
employe = employes_manager.read(2)
print(employe)

# Mettre à jour un employé existant
update = employes_manager.update(2, "Durand", "Paul", 3500.00, 2)
print(employes_manager.read(2))


# Supprimer un employé existant
employes_manager.delete(1)


