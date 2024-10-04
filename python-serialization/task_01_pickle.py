import pickle

# Définition de la classe CustomObject
class CustomObject:
    def __init__(self, name, age, is_student):
        """
        Initialisation des attributs d'un objet CustomObject.
        
        :param name: Nom de la personne
        :param age: Âge de la personne
        :param is_student: Statut étudiant (booléen)
        """
        self.name = name
        self.age = age
        self.is_student = is_student

    def display(self):
        """
        Affiche les attributs de l'objet CustomObject.
        """
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Is Student: {self.is_student}")

    def serialize(self, filename):
        """
        Sérialise l'objet courant et l'enregistre dans un fichier avec pickle.
        
        :param filename: Nom du fichier de sortie
        """
        with open(filename, 'wb') as file:
            pickle.dump(self, file)  # Sérialiser l'objet et l'enregistrer dans un fichier

    @classmethod
    def deserialize(cls, filename):
        """
        Désérialise un objet depuis un fichier pickle et retourne une instance de CustomObject.
        
        :param filename: Nom du fichier de pickle
        :return: Instance désérialisée de CustomObject
        """
        try:
            with open(filename, 'rb') as file:
                return pickle.load(file)  # Charger l'objet sérialisé depuis le fichier
        except FileNotFoundError:
            print("Le fichier spécifié est introuvable.")
            return None
