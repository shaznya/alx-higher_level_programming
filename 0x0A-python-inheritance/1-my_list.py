#!/usr/bin/python3
"""
This module defines a MyList class that inherits from list.
The MyList class includes a method to print the list in ascending order.
"""


class MyList(list):
    """
    A class that inherits from list and includes a method to print
    the list in ascending order.

    Methods:
        print_sorted(self): Prints the list, but sorted in ascending order.
    """

    def print_sorted(self):
        """
        Print the elements of the list in ascending order.

        This method sorts the list and prints it without modifying
        the original list.

        Examples:
        >>> my_list = MyList([3, 1, 2])
        >>> my_list.print_sorted()
        [1, 2, 3]
        >>> my_list = MyList([5, 7, 2, 4])
        >>> my_list.print_sorted()
        [2, 4, 5, 7]
        >>> my_list = MyList([10, 5])
        >>> my_list.print_sorted()
        [5, 10]
        >>> my_list = MyList([])
        >>> my_list.print_sorted()
        []
        """
        sorted_list = sorted(self)
        print(sorted_list)
