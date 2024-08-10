#!/usr/bin/python3
"""
Module for Rectangle class that inherits from BaseGeometry.
"""
from base_geometry import BaseGeometry

class Rectangle(BaseGeometry):
    """
    A Rectangle class that inherits from BaseGeometry.
    """

    def __init__(self, width, height):
        """
        Initialize the rectangle with width and height, validating the inputs.

        Args:
            width (int): The width of the rectangle.
            height (int): The height of the rectangle.
        """
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def __str__(self):
        """
        Return the string representation of the Rectangle.
        """
        return "[Rectangle] {}/{}".format(self.__width, self.__height)

    def area(self):
        """
        Return the area of the Rectangle.
        """
        return self.__width * self.__height
