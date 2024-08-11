#!/usr/bin/python3
"""
This module defines a class `Square` that inherits from `Rectangle`.
"""

from rectangle import Rectangle


class Square(Rectangle):
    """
    A class representing a square, inheriting from `Rectangle`.
    """

    def __init__(self, size):
        """
        Initializes a new Square instance.

        Args:
            size (int): The size of the square.

        Validates size to ensure it is a positive integer.
        """
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def area(self):
        """
        Calculates the area of the square.

        Returns:
            int: The area of the square.
        """
        return self.__size * self.__size

    def __str__(self):
        """
        Returns a string representation of the square.

        Returns:
            str: The description of the square.
        """
        return f"[Square] {self.__size}/{self.__size}"
