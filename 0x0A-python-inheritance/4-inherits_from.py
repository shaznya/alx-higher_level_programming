#!/usr/bin/python3
"""
This module checks if an object is an instance of a class.
"""


def inherits_from(obj, a_class):
    """

    Check if the object is an instance of a class from the specified class.

    Args:
        obj: The object to check.
        a_class: The class to check against.

    Returns:
        bool: True; otherwise False.
    """
    return isinstance(obj, a_class) and type(obj) is not a_class
