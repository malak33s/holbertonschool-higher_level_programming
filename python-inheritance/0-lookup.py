#!/usr/bin/python3
"""
Module 0-lookup
fonction qui retourne la liste des attributs and methodes d'un objet.
"""


def lookup(obj):
    """
    Returns the list of available attributes and methods of an object.

    Args:
        obj: The object to inspect.

    Returns:
        A list of the available attributes and methods of the object.
    """
    return dir(obj)
