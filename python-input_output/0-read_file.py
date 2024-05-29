#!/usr/bin/python3
"""
function read a text file and print its contents.
"""

def read_file(filename=""):
    """ read a text file and print
    args:
    file str): name of file.
    """
    with open(filename, 'r', encoding='utf-8') as f:
        print(f.read(), end='')

