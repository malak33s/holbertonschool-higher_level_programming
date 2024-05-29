#!/usr/bin/python3
"""
function to append a string to a text.
"""

def append_write(filename="", text=""):
    """
    the name of file to append, text to append file
    """
    with open(filename, 'a', encoding='utf-8') as f:
        return f.write(text)
