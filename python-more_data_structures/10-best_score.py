#!/usr/bin/python3
def best_score(a_dictionary):
    if not isinstance(a_dictionary, dict) or len(a_dictionary) == 0:
        return None

    result = list(a_dictionary.keys())[0]
    temp = a_dictionary[result]
    for one, two in a_dictionary.items():
        if two > temp:
            deb = two
            result = one
    return (result)
