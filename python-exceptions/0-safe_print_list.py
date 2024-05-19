#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):
    try:
        for a in range(x):
            print(my_list[a], end="")
    except IndexError:
        x = a
    finally:
        print()
        return x
