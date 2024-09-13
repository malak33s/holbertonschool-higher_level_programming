#!/usr/bin/python3
""""Define a function that prints a square with the character #"""


def print_square(size):
    """Print a square with the character #

    size must be an integer

    Raises:
        TypeError: size must be an integer
        ValueError: size must be >= 0
    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    for i in range(size):
        [print("#", end="") for j in range(size)]
        print("")
