#!/usr/bin/python3
"""
This module defines a function that prints a square of `#` characters.
"""


def print_square(size):
    """
    Prints a square with the character `#`.

    Args:
        size (int): The length of the square's side.

    Raises:
        TypeError: If size is not an integer or if it is a float less than 0.
        ValueError: If size is less than 0.
    """
    if type(size) is not int:
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    if isinstance(size, float) and size < 0:
        raise TypeError("size must be an integer")

    for _ in range(size):
        print("#" * size)
