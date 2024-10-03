#!/usr/bin/python3
"""Defines a function to write an object to a JSON file."""

import json


def save_to_json_file(my_obj, filename):
    """Writes an Object to a text file, using a JSON representation.

    Args:
        my_obj: The object to be written to the JSON file.
        filename: The name of the file to write to.
    """
    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(my_obj, f)
