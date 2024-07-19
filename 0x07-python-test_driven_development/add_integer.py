#!/usr/bin/python3
"""
This module defines a function that adds two integers or floats.
"""


def add_integer(a, b=98):
    """
    Adds two integers or floats and returns the result as an integer.

    Args:
        a (int, float): The first number.
        b (int, float): The second number, defaults to 98.

    Returns:
        int: The addition of `a` and `b`, cast to an integer.

    Raises:
        TypeError: If `a` or `b` are not integers or floats.
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    return int(a) + int(b)
