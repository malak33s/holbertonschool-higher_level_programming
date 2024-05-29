#!/usr/bin/python3
"""
a function to create an object from a json file.
"""

import json

def load_from_json_file(filename):
    """
    create an object from a json file.

    Args:
        file the name of the file containing the json string.

    Returns:
        object created from the json file.
    """
    with open(filename, 'r', encoding='utf-8') as f:
        return json.load(f)

