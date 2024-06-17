#!/usr/bin/python3
import math


class MagicClass:

    """A class that represents a circle with a given radius."""

    def __init__(self, radius=0):
        """Initialize the MagicClass with a radius."""
        self.radius = radius

    @property
    def radius(self):
        """Get the radius of the circle."""
        return self.__radius

    @radius.setter
    def radius(self, value):
        """Set the radius of the circle.

        Args:
            value (int or float): The radius value.

        Raises:
            TypeError: If the value is not an integer or float.
            ValueError: If the value is less than 0.
        """
        if not isinstance(value, (int, float)):
            raise TypeError("radius must be a number")
        if value < 0:
            raise ValueError("radius must be >= 0")
        self.__radius = value

    def area(self):
        """Calculate the area of the circle.

        Returns:
            float: The area of the circle.
        """
        return math.pi * self.radius**2

    def circumference(self):
        """Calculate the circumference of the circle.

        Returns:
            float: The circumference of the circle.
        """
        return 2 * math.pi * self.radius


if __name__ == "__main__":
    circle = MagicClass(3)
    print("Area:", circle.area())
    print("Circumference:", circle.circumference())
