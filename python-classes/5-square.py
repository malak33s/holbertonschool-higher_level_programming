#!/usr/bin/python3
"""Define a class """


class Square:
    """create a Square class"""

    def __init__(self, size=0):
        """ Init a new square and this  size

        Args:
        size (int) size of a square
        """
        self.size = size

    @property
    def size(self):
        """set current size square"""
        return (self.__size)

    @size.setter
    def size(self, value):
        """ value is lenght of square"""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """return size of square"""
        return (self.__size * self.__size)
    
    def my_print(self):
        """print the square with #"""
        for i in range(0, self.__size):
            [print("#", end="") for j in range(self.__size)]
            print("")
        if self.__size == 0:
            print("")
