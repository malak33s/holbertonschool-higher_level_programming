#!/usr/bin/python3
"""Script that adds all arguments to a Python list and saves them to a JSON file."""

import sys
import json

def save_to_json_file(my_obj, filename):
    """Writes an Object to a text file, using a JSON representation."""
    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(my_obj, f)

def load_from_json_file(filename):
    """Creates an Object from a 'JSON file'."""
    with open(filename, 'r', encoding='utf-8') as f:
        return json.load(f)

if __name__ == "__main__":
    filename = "add_item.json"
    
    # Load existing items from the JSON file if it exists
    try:
        items = load_from_json_file(filename)
    except FileNotFoundError:
        items = []

    # Add command line arguments to the list (excluding the script name)
    items.extend(sys.argv[1:])

    # Save the updated list back to the JSON file
    save_to_json_file(items, filename)
