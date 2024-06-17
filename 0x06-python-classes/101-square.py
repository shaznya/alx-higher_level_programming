#!/usr/bin/env python3

class Square:
    """A class representing a square."""

    def __init__(self, size=0, position=(0, 0)):
        """Initialize a square with a size and position.

        Args:
            size (int, optional): The size of the square (default is 0).
            position (tuple, optional)
        """
        self.size = size
        self.position = position

    @property
    def size(self):
        """Get the size of the square."""
        return self.__size

    @size.setter
    def size(self, value):
        """Set the size of the square.

        Args:
            value (int): The size of the square.

        Raises:
            TypeError: If the size is not an integer.
            ValueError: If the size is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """Get the position of the square."""
        return self.__position

    @position.setter
    def position(self, value):
        """Set the position of the square.

        Args:
            value (tuple): The position of the square.

        Raises:
            TypeError: If the position is not a tuple of 2 positive integers.
        """
        if not isinstance(value, tuple) or len(value) != 2 \
                or not all(isinstance(x, int) for x in value) \
                or not all(x >= 0 for x in value):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """Calculate the area of the square."""
        return self.size ** 2

    def my_print(self):
        """Print the square with the character '#'."""
        if self.size == 0:
            print()
            return

        for _ in range(self.position[1]):
            print()
        for _ in range(self.size):
            print(" " * self.position[0] + "#" * self.size)

    def __str__(self):
        """Return a string representation of the square."""
        return self.my_print()


# Example usage
if __name__ == "__main__":
    square = Square(3, (2, 1))
    print("Area:", square.area())
    square.my_print()

    print("\nChanging size and position:")
    square.size = 5
    square.position = (0, 0)
    print("Area:", square.area())
    square.my_print()
