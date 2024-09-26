#!/usr/bin/python3
"""
Module 9-rectangle
Defines a Rectangle class that inherits from BaseGeometry
"""

BaseGeometry = __import__('7-base_geometry').BaseGeometry

class Rectangle(BaseGeometry):
    """A class to define a rectangle, inherits from BaseGeometry"""

    def __init__(self, width, height):
        """Initialize rectangle with width and height, validated by integer_validator"""
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """Calculate the area of the rectangle"""
        return self.__width * self.__height

    def __str__(self):
        """Return a string representation of the rectangle"""
        return f"[Rectangle] {self.__width}/{self.__height}"
