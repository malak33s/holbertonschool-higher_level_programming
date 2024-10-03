#!/usr/bin/python3
"""
Module 10-square
Defines a Square class that inherits from Rectangle
"""

Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """A class to define a square, inherits from Rectangle"""

    def __init__(self, size):
        """Initialize square with size, validated by integer_validator"""
        self.integer_validator("size", size)
        self.__size = size
        # the parent class with width and height being the same
        super().__init__(size, size)

    def area(self):
        """Calculate the area of the square"""
        return self.__size * self.__size
