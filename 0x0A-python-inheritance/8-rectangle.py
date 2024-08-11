#!/usr/bin/python3
"""
This module defines a class `Rectangle` that inherits from `BaseGeometry`.
"""

from base_geometry import BaseGeometry


class Rectangle(BaseGeometry):
    """
    A class representing a rectangle, inheriting from `BaseGeometry`.
    """

    def __init__(self, width, height):
        """
        Initializes a new Rectangle instance.

        Args:
            width (int): The width of the rectangle.
            height (int): The height of the rectangle.

        Validates width and height to ensure they are positive integers.
        """
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height
