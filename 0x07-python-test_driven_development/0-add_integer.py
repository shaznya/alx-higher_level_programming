#!/usr/bin/python3
def add_integer(a, b=98):
    """
    Adds two integers.

    Args:
        a (int or float): First integer or float.
        b (int or float, optional): Second integer or float. Defaults to 98.

    Raises:
        TypeError: If either a or b is not an integer or float.

    Returns:
        int: The sum of a and b, casted to an integer.
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")

    return int(a) + int(b)
