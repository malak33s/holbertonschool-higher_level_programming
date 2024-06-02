#!/usr/bin/python3
"""Define serialization and deserialization CSV"""

import csv
import json


def convert_csv_to_json(csv_filename):
    """Convert CSV to JSON

    Args:
        filename: name of the file
    """
    try:
        dict_list = []
        
        with open(csv_filename, "r") as f:
            reader = csv.DictReader(f)
            for cpt in reader:
                dict_list.append(cpt)
            
        with open("data.json", "w") as f:
            json.dump(dict_list, f)
        
        return True
    
    except FileNotFoundError:
        return False
