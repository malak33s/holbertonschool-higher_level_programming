#!/usr/bin/python3
"""
a function to write a string to a text file.
"""

def write_file(filename="", text=""):
    """ a string to text file and return the num character written
    """
    with open(filename, 'w', encoding='utf-8') as f:
        return f.write(text)

