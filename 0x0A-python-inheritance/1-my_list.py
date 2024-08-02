#!/usr/bin/python3
"""
This module defines the MyList class that inherits from list.
"""

class MyList(list):
    """
    A class that inherits from list and provides a method to print the list in sorted order.
    """

    def print_sorted(self):
        """
        Print the list in ascending order.
        """
        print(sorted(self))
