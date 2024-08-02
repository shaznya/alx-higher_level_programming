#!/usr/bin/python3
"""
This module defines a custom list class that inherits from the built-in list.
"""

class MyList(list):
    """
    MyList is a subclass of the built-in list class, 
    providing additional functionality to print the list in sorted order.
    """

    def print_sorted(self):
        """
        Prints the elements of the list in ascending order.

        This method does not modify the original list.
        """
        sorted_list = self[:]
        for i in range(len(sorted_list)):
            for j in range(len(sorted_list) - 1):
                if sorted_list[j] > sorted_list[j + 1]:
                    sorted_list[j], sorted_list[j + 1] = sorted_list[j + 1], sorted_list[j]
        print(sorted_list)
