#!/usr/bin/python3
"""
This module defines a class MyList that inherits from the built-in list class.
It includes a method to print the list in sorted order.
"""

class MyList(list):
    """
    MyList class that inherits from list and adds a method to print sorted list.
    """

    def print_sorted(self):
        """
        Print the elements of the list in ascending order.
        """
        print(sorted(self))
