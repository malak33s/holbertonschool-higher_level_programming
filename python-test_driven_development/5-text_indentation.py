#!/usr/bin/python3
"""create a function a text_indentation"""


def text_indentation(text):
    """Printed a text with 2 new lines after two characters: ., ? and :

    Raises:
        TypeError: text must be a string
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    idx = 0
    while idx < len(text) and text[idx] == ' ':
        idx += 1

    while idx < len(text):
        print(text[idx], end="")
        if text[idx] == "\n" or text[idx] in ".?:":
            if text[idx] in ".?:":
                print("\n")
            idx += 1
            while idx < len(text) and text[idx] == ' ':
                idx += 1
            continue
        idx += 1
