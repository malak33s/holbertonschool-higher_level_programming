#!/usr/bin/python3
"""
function that writing an object to a textfile json representation.
"""

import json

def save_to_json_file(my_obj, filename):
    """
    write a object to json representation.
    Args:
        my_obj: the object to be serialized and written to the file.
    """
    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(my_obj, f)

