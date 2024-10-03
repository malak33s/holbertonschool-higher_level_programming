#!/usr/bin/python3
"""
This module contains a function that reads a UTF8 text file
and prints its content to stdout.
"""


def read_file(filename=""):
    """
Reads a UTF8 text file and prints its content to stdout.

    Args:
        filename (str): The name of the file to read.
    """
    with open(filename, encoding="utf-8") as f:
        print(f.read(), end="")