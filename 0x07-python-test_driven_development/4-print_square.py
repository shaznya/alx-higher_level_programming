#!/usr/bin/python3
"""
Module to print a square with the character #.
"""

def print_square(size):
    """
    Prints a square with the character #.

    Args:
        size (int): The length of the square's sides.

    Raises:
        TypeError: If size is not an integer or if size is a float and less than 0.
        ValueError: If size is less than 0.
    """
    if isinstance(size, float):
        if size < 0:
            raise TypeError("size must be an integer")
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")

    for _ in range(size):
        print('#' * size)
