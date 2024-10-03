#!/usr/bin/python3
"""Defines a text file-writing function"""

def write_file(filename="", text=""):
    """Writes a string to a text file and returns the number of characters written."""
    
    # Ouvre le fichier en mode écriture ('w'), ce qui crée le fichier s'il n'existe pas
    # ou écrase son contenu s'il existe déjà
    with open(filename, 'w', encoding="utf-8") as f:
        i = f.write(text)  # Écrit le texte dans le fichier et stocke le nombre de caractères écrits
    return i  # Retourne le nombre de caractères écrits
