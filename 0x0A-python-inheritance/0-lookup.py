#!/usr/bin/python3
"""
This module provides a function to retrieve the list of attributes and methods
of an object.
"""


def lookup(obj):
    """
    Return a list of available attributes and methods of an object.

    Args:
        obj: The object to inspect.

    Returns:
        list: A list of strings representing the names of available attributes
        and methods of the object.
    """
    return dir(obj)
