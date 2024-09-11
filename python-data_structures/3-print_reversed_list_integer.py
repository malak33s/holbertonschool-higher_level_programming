#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    """Function that prints all integers of a list in reverse order."""
    if my_list:  # Vérifie si la liste n'est pas vide
        for number in my_list[::-1]:  # Parcours de la liste inversée
            print("{:d}".format(number))  # Impression formatée de l'entier
