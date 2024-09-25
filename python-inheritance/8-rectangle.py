#!/usr/bin/python3
"""
Module 8-rectangle
Defines a Rectangle class that inherits from BaseGeometry
"""

BaseGeometry = __import__('7-base_geometry').BaseGeometry

class Rectangle(BaseGeometry):
    """Class that defines a rectangle and inherits from BaseGeometry"""

    def __init__(self, width, height):
        """Initialize the rectangle with width and height, validated by integer_validator"""
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width  # private attribute
        self.__height = height  # private attribute
