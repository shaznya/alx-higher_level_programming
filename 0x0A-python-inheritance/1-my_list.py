#!/usr/bin/python3
"""
This module defines a class MyList that inherits from the built-in list class.
"""


class MyList(list):
    """
    MyList class that inherits from list.
    """

    def print_sorted(self):
        """
        Print the elements of the list in ascending order.
        """
        sorted_list = sorted(self)
        print(sorted_list)
