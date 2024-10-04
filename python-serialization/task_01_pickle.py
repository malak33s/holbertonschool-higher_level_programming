import pickle


class CustomObject:
    """
    Classe personnalisée représentant un objet avec des attributs nom, âge
    et étudiant.
    """

    def __init__(self, name, age, is_student):
        """
        Constructeur de la classe CustomObject.

        :param name: Nom de l'objet (str)
        :param age: Âge de l'objet (int)
        :param is_student: Statut étudiant de l'objet (bool)
        """
        self.name = name
        self.age = age
        self.is_student = is_student

    def display(self):
        """
        Affiche les attributs de l'objet dans un format lisible.
        """
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Is Student: {self.is_student}")

    def serialize(self, filename):
        """
        Sérialise l'instance actuelle de l'objet et l'enregistre dans le
        fichier spécifié.

        :param filename: Nom du fichier pour enregistrer l'objet sérialisé
        :return: None
        """
        try:
            with open(filename, 'wb') as file:
                # Enregistrer l'objet sérialisé dans le fichier
                pickle.dump(self, file)
        except Exception as e:
            print(f"Erreur lors de la sérialisation : {e}")

    @classmethod
    def deserialize(cls, filename):
        """
        Désérialise un fichier et retourne une instance de CustomObject.

        :param filename: Nom du fichier à désérialiser
        :return: Instance de CustomObject ou None en cas d'erreur
        """
        try:
            with open(filename, 'rb') as file:
                # Charger et retourner l'objet désérialisé
                return pickle.load(file)
        except (FileNotFoundError, pickle.UnpicklingError) as e:
            print(f"Erreur lors de la désérialisation : {e}")
            return None
