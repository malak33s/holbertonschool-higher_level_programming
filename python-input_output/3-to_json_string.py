#!/usr/bin/python3
"""Defines a function to convert an object to a JSON string."""

import json


def to_json_string(my_obj):
    """Returns the JSON representation of an object.

    Args:
        my_obj: The object to be converted to JSON.

    Returns:
        The JSON representation as a string.
    """
    return json.dumps(my_obj)
