#!/usr/bin/python3
"""Define a class """


class Square:
    """create a Square class"""

    def __init__(self, size=0):
        """ Init a new square and this  size"""

        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """def of the arrea of square"""
        return (self.__size * self.__size)
