#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    list_number = argv[1:]
    result = sum(int(number) for number in list_number)
    print(result)
