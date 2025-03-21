#!/usr/bin/python3

print("".join("{:c}".format(letter) for letter in range(97, 123)
              if letter not in (101, 113)), end="")
