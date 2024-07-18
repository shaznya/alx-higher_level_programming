#!/usr/bin/python3

"""
Module for adding two integers.
"""

def add_integer(a, b=98):
    """
    Add two integers.

    Parameters:
    a: int or float, the first number.
    b: int or float, the second number (default is 98).

    Returns:
    int: Sum of the two numbers.

    Raises:
    TypeError: If `a` or `b` are not integers or floats.

    Example:
    >>> add_integer(1, 2)
    3
    >>> add_integer(100, -2)
    98
    >>> add_integer(2)
    100
    >>> add_integer(100.3, -2)
    98
    >>> add_integer("School", 2)
    Traceback (most recent call last):
        ...
    TypeError: a must be an integer
    >>> add_integer(4, "School")
    Traceback (most recent call last):
        ...
    TypeError: b must be an integer
    >>> add_integer(None)
    Traceback (most recent call last):
        ...
    TypeError: a must be an integer
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    return int(a) + int(b)
