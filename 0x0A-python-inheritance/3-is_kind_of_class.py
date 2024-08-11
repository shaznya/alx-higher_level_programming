#!/usr/bin/python3
"""
This module checks if an object is an instance of a specified class.
"""


def is_kind_of_class(obj, a_class):
    """
    Check if the object is an instance of the specified class.

    Args:
        obj: The object to check.
        a_class: The class to check against.

    Returns:
    bool: True;
    otherwise False.
    """
    return isinstance(obj, a_class)
