#!/usr/bin/python3
"""
This module defines a function `is_same_class` that checks if an object
is an instance of a specified class.
"""


def is_same_class(obj, a_class):
    """
    Return True if the object is exactly an instance of the specified class;
    otherwise return False.

    Args:
        obj: The object to check.
        a_class: The class to compare the object against.

    Returns:
        bool: True if obj is an instance of a_class, else False.
    """
    return type(obj) is a_class
