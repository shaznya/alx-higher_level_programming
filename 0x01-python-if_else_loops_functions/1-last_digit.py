#!/usr/bin/python3
import random

number = random.randint(-10000, 10000)
last_digit = abs(number) % 10

string = "Last digit of {} is {}".format(number, last_digit)

if number < 0:
    last_digit = -last_digit

output = f"{string} and is"

if last_digit > 5:
    print(output, "greater than 5")
elif last_digit == 0:
    print(output, "0")
else:
    print(output, "less than 6 and not 0")

