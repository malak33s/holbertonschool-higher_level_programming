#!/usr/bin/python3
"""
Module 3-is_kind_of_class
function checks if an object is an instance of, or if the object
is an instance of a class, the specified class.
"""


def is_kind_of_class(obj, a_class):
    """
    Returns True if the object, or if the object is an instance in a
    class, the specified class.

    Args:
        obj: The object to check.
        a_class: The class to compare against.

    Returns:
    """
    return isinstance(obj, a_class)
