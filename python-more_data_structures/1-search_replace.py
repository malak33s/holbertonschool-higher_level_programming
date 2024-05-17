#!/usr/bin/python3
def search_replace(my_list, search, replace):
    new_lst = [replace if elm == search else elm for elm in my_list]
    return new_lst
