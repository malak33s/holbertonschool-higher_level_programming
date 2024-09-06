#!/usr/bin/python3
def print_last_digit(n):
    lastDigit = abs(n) % 10
    print(lastDigit, end="")
    return lastDigit
