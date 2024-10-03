#!/usr/bin/python3
"""Defines a text file-apend function"""


def append_write(filename="", text=""):
    """Appends string end a text fil and return number of chara add"""
    with open(filename, "a", encoding="utf-8") as f:
        return f.write(text)
