#!/usr/bin/python3
"""Defines two integers for the addition function"""


def add_integer(a, b=98):
    """Returns a + b

    a and b must be int or float

    Raises:
        TypeError: if a or b is a non-integers and non-floats
    """
    if ((not isinstance(a, int) and not isinstance(a, float))):
        raise TypeError("a must be an integer")
    if ((not isinstance(b, int) and not isinstance(b, float))):
        raise TypeError("b must be an integer")

    return (int(a) + int(b))
