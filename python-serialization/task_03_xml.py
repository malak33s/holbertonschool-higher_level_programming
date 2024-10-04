import xml.etree.ElementTree as ET

# Fonction pour sérialiser un dictionnaire Python en XML
def serialize_to_xml(dictionary, filename):
    """
    Sérialise un dictionnaire Python en XML et l'enregistre dans un fichier.
    
    :param dictionary: Dictionnaire à sérialiser
    :param filename: Nom du fichier de sortie XML
    """
    # Création de l'élément racine
    root = ET.Element("data")

    # Ajout des éléments au fichier XML
    for key, value in dictionary.items():
        element = ET.SubElement(root, key)  # Créer un sous-élément pour chaque clé du dictionnaire
        element.text = str(value)  # Convertir la valeur en texte

    # Enregistrement de l'arbre XML dans un fichier
    tree = ET.ElementTree(root)
    tree.write(filename)  # Sauvegarder l'arbre dans le fichier


# Fonction pour désérialiser un fichier XML en dictionnaire Python
def deserialize_from_xml(filename):
    """
    Charge et désérialise un fichier XML en un dictionnaire Python.
    
    :param filename: Nom du fichier XML à charger
    :return: Dictionnaire Python contenant les données désérialisées
    """
    try:
        tree = ET.parse(filename)  # Charger et analyser le fichier XML
        root = tree.getroot()

        # Convertir l'arbre XML en dictionnaire
        result = {child.tag: child.text for child in root}

        return result  # Retourner le dictionnaire

    except FileNotFoundError:
        print(f"Le fichier {filename} est introuvable.")
        return None  # Retourner None en cas d'erreur
