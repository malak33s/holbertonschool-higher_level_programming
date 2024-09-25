#!/usr/bin/python3
"""
Module 7-base_geometry
Defines a class BaseGeometry with an area method and an integer validator
"""

class BaseGeometry:
    """Class BaseGeometry"""

    def area(self):
        """
        Raises an exception to indicate that the method is not implemented
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        Validates that value is a positive integer

        Args:
            name (str): Name of the value, assumed to be a string.
            value (int): The value to validate.

        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is less than or equal to 0.
        """
        if not isinstance(value, int):
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
