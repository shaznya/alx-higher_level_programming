#!/usr/bin/python3
"""
This module defines the add_integer function.
"""

def add_integer(a, b=98):
    """
    Adds two integers and returns the result.

    Args:
        a (int, float): The first integer.
        b (int, float): The second integer, defaults to 98.

    Raises:
        TypeError: If a or b are not integers or floats.

    Returns:
        int: The sum of a and b.
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    return int(a) + int(b)
