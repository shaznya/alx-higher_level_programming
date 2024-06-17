#!/usr/bin/python3
"""
Defines a class Square with private size attribute.
"""


class Square:
    """
    This class defines a square.

    Attributes:
        __size (int): The size of the square.
    """

    def __init__(self, size=0):
        """
        Initializes a square with a given size.

        Args:
            size (int): The size of the square (default 0).
        """
        self.size = size

    @property
    def size(self):
        """
        Retrieves the size of the square.

        Returns:
            int: The size of the square.
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        Sets the size of the square.

        Args:
            value (int): The size of the square.

        Raises:
            TypeError: If size is not a number (float or integer).
            ValueError: If size is less than 0.
        """
        if not isinstance(value, (int, float)):
            raise TypeError("size must be a number")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def area(self):
        """
        Calculates the area of the square.

        Returns:
            int: The area of the square.
        """
        return self.__size ** 2

    def __eq__(self, other):
        """
        Checks if two squares are equal in size.

        Args:
            other (Square): The other square to compare.

        Returns:
            bool: True if both squares have the same area, False otherwise.
        """
        if isinstance(other, Square):
            return self.area() == other.area()
        return False

    def __ne__(self, other):
        """
        Checks if two squares are not equal in size.

        Args:
            other (Square): The other square to compare.

        Returns:
            bool: True if both squares have different areas, False otherwise.
        """
        if isinstance(other, Square):
            return self.area() != other.area()
        return True

    def __gt__(self, other):
        """
        Checks if the area of one square is greater.

        Args:
            other (Square): The other square to compare.

        Returns:
            bool: True if the area of the first square is greater.
        """
        if isinstance(other, Square):
            return self.area() > other.area()
        return False

    def __ge__(self, other):
        """
        Checks if the area of one square is greater than or equal to.

        Args:
            other (Square): The other square to compare.

        Returns:
            bool: True if the area of the first square is greater or equal.
        """
        if isinstance(other, Square):
            return self.area() >= other.area()
        return False

    def __lt__(self, other):
        """
        Checks if the area of one square.

        Args:
            other (Square): The other square to compare.

        Returns:
            bool: True if the area of the first square is less.
        """
        if isinstance(other, Square):
            return self.area() < other.area()
        return False

    def __le__(self, other):
        """
        Checks if the area of one square.

        Args:
            other (Square): The other square to compare.

        Returns:
            bool: True if the area of the first square is less or equal.
        """
        if isinstance(other, Square):
            return self.area() <= other.area()
        return False


if __name__ == "__main__":
    pass
