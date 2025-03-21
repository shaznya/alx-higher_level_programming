#!/usr/bin/python3

# Print lowercase ASCII alphabet excluding 'q' and 'e' in one print statement
print("".join(
    "{:c}".format(letter) for letter in range(97, 123)
    if letter not in (113, 101)
), end="")
