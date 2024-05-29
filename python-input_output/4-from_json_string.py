#!/usr/bin/python3
"""
function to get the object from a json string.
"""

import json

def from_json_string(my_str):
    """
    return an object represented by a json string.

    Args:
        my_str (str): string to be deserialized.
    """
    return json.loads(my_str)

