#!/usr/bin/python3
import sys
import json
# import the functions from the previous tasks
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

def main():
    """
    add all command-line args to a list and save them to a JSON file
    if the file do not exist its will be created.
    """
    filename = "add_item.json"

    try:
        items = load_from_json_file(filename)
    except (FileNotFoundError, json.JSONDecodeError):
        items = []

    items.extend(sys.argv[1:])
    save_to_json_file(items, filename)

if __name__ == "__main__":
    main()

