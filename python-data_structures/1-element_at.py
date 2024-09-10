#!/usr/bin/python3
def element_at(my_list, idx):
    """prendre un element d'une liste d'un index specifique"""
    if idx < 0 or idx >= len(my_list):
        return None
    return my_list[idx]
