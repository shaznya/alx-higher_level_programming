#!/usr/bin/python3
"""
This module defines a class `Rectangle` that inherits from `BaseGeometry`,
with methods for area calculation and string representation.
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

    def area(self):
        """
        Calculates the area of the rectangle.

        Returns:
            int: The area of the rectangle.
        """
        return self.__width * self.__height

    def __str__(self):
        """
        Returns a string representation of the rectangle.

        Returns:
            str: The description of the rectangle.
        """
        return f"[Rectangle] {self.__width}/{self.__height}"

    def __repr__(self):
        """
        Returns a string that represents the rectangle.

        Returns:
            str: A string representation of the rectangle object.
        """
        return f"Rectangle({self.__width}, {self.__height})"
