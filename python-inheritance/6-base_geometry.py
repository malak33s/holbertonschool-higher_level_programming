#!/usr/bin/python3
"""
Module 6-base_geometry
Defines a class BaseGeometry with a method area that raises an exception
"""


class BaseGeometry:
    """Class BaseGeometry with a method area"""

    def area(self):
        """exception to indicate that the method"""
        raise Exception("area() is not implemented")
