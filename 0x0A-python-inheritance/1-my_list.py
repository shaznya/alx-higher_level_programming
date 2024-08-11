#!/usr/bin/python3
"""
This module defines a class `MyList` that inherits from the built-in
`list` class.
"""


class MyList(list):
    """
    A class that inherits from the built-in `list` class and
    includes a method to print the list in ascending sorted order.
    """

    def print_sorted(self):
        """
        Prints the list in ascending sorted order.
        """
        sorted_list = sorted(self)
        print(sorted_list)
