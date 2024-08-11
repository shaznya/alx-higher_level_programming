#!/usr/bin/python3
"""
This module defines a class `BaseGeometry` with an `area` method that
raises an exception.
"""


class BaseGeometry:
    """
    A class representing basic geometric concepts.
    """

    def area(self):
        """
        Raises an Exception with the message 'area() is not implemented'.
        """
        raise Exception("area() is not implemented")
