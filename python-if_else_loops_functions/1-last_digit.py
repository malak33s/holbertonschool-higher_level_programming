#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
lastDigit = abs(number) % 10

if number < 0:
    lastDigit *= -1

print("Last digit of {} is {} and ".format(number, lastDigit), end="")
if lastDigit > 5:
    print("is greater than 5")
elif lastDigit == 0:
    print("is 0")
else:
    print("is less than 6 and not 0")
