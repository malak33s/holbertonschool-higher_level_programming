import csv
import json

# Fonction pour convertir un fichier CSV en JSON
def convert_csv_to_json(csv_filename):
    """
    Convertit les données d'un fichier CSV en un fichier JSON.
    
    :param csv_filename: Nom du fichier CSV à convertir
    :return: True si la conversion réussit, False en cas d'erreur
    """
    try:
        data = []
        # Ouverture et lecture du fichier CSV
        with open(csv_filename, 'r') as csv_file:
            reader = csv.DictReader(csv_file)  # Utilisation de DictReader pour convertir chaque ligne en dictionnaire
            for row in reader:
                data.append(row)  # Ajouter chaque ligne à la liste des données

        # Enregistrement des données dans un fichier JSON
        with open('data.json', 'w') as json_file:
            json.dump(data, json_file, indent=4)  # Sérialiser et écrire les données au format JSON

        return True  # Conversion réussie

    except FileNotFoundError:
        print(f"Le fichier {csv_filename} est introuvable.")
        return False  # Retourner False en cas d'erreur
