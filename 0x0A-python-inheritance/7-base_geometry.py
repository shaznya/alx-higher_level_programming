#!/usr/bin/python3
"""
Module defining the BaseGeometry class.
"""

class BaseGeometry:
    """
    BaseGeometry class with methods for area and integer validation.
    """

    def area(self):
        """
        Method that raises an Exception with the message area() is not implemented.
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        Method to validate value as an integer greater than 0.
        
        Args:
            name (str): The name of the parameter.
            value (int): The value to be validated.

        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is less than or equal to 0.
        """
        if not isinstance(value, int):
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
