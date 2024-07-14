#!/usr/bin/python3
"""
Module to add integers.
"""


def add_integer(a, b=98):

    """
    Adds two integers.
    Args:
    a: First integer or float.
    b: Second integer or float, defaults to 98.
    Returns:
    The integer addition of a and b.
    Raises:
    TypeError: If either of a or b is not an integer or float.
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    return int(a) + int(b)
