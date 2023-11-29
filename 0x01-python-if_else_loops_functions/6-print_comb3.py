#!/usr/bin/python3

for tens_digit in range(10):
    for units_digit in range(tens_digit, 10):
        if tens_digit != units_digit:
            print("{:d}{:d}".format(tens_digit, units_digit), end=', ' if tens_digit != 9 or units_digit != 9 else '\n')
