#!/usr/bin/python3
"""Defines a text file-writing function"""


def write_file(filename="", text=""):
    """returns the number of characters written."""

    with open(filename, 'w', encoding="utf-8") as f:
        i = f.write(text)  # texte in fichier & stock nombre de cara
    return i  # Retourne le nombre de caractères écrits
