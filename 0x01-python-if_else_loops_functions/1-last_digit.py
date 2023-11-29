#!/usr/bin/python3
import random

# Generate a random signed number between -10000 and 10000
number = random.randint(-10000, 10000)

# Extract the last digit of the absolute value of the number
last_digit = abs(number) % 10

# Adjust the last digit for negative numbers
if number < 0:
    last_digit = -last_digit

# Create a formatted string describing the number and its last digit
output_string = f"Last digit of {number} is {last_digit} and is"

# Determine and print the result based on the conditions
if last_digit > 5:
    print(output_string, "greater than 5")
elif last_digit == 0:
    print(output_string, "0")
else:
    print(output_string, "less than 6 and not 0")
