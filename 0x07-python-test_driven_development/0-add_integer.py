#!/usr/bin/python3
"""
This module defines a function `add_integer` that adds two integers.
"""


def add_integer(a, b=98):
    """
    Adds two integers or floats.

    Args:
        a (int, float): The first value.
        b (int, float): The second value (default is 98).

    Returns:
        int: The sum of a and b, cast to an integer.

    Raises:
        TypeError: If a or b are not integers or floats.
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")

    return int(a) + int(b)
