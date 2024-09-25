#!/usr/bin/python3
"""
Module 6-base_geometry
Defines a class BaseGeometry with a method area that raises an exception
"""

class BaseGeometry:
    """Class BaseGeometry with a method area"""
    
    def area(self):
        """Raises an exception to indicate that the method is not implemented"""
        raise Exception("area() is not implemented")
