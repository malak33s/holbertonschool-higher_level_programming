#!/usr/bin/python3
import sys
import os

# Import the required functions from the respective modules
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

# Define the filename for the JSON file
filename = "add_item.json"

# Check if the file exists. If it does, load the existing list; otherwise, start with an empty list
if os.path.exists(filename):
    my_list = load_from_json_file(filename)
else:
    my_list = []

# Extend the list with the arguments passed to the script (skipping the script name itself)
my_list.extend(sys.argv[1:])

# Save the updated list back to the file
save_to_json_file(my_list, filename)

