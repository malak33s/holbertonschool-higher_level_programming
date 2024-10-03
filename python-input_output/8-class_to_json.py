#!/usr/bin/python3
"""Defines a function that converts a class instance to a dictionary."""


def class_to_json(obj):
    """Returns the dictionary description with simple data structures
    for JSON serialization of an object.

    Args:
        obj: An instance of a class.

    Returns:
        A dictionary description of the instance suitable for
        JSON serialization.
    """
    return obj.__dict__
