import json


def serialize_and_save_to_file(data, filename):
    """
    Sérialise les données sous forme de JSON et les enregistre dans le fichier
    spécifié.

    :param data: Dictionnaire Python à sérialiser
    :param filename: Nom du fichier de sortie
    """
    with open(filename, 'w') as file:
        json.dump(data, file)  # données sérialisées dans JSON


def load_and_deserialize(filename):
    """
    JSON deseri in dict Python.

    :param filename: Nom du fichier JSON à charger
    :return: Dictionnaire Python contenant les données désérialisées
    """
    with open(filename, 'r') as file:
        return json.load(file)  # données convertir dict
