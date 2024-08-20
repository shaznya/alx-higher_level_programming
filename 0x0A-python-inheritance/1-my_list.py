#!/usr/bin/python3
"""
This module defines a class MyList that inherits from the built-in
list class.
"""

class MyList(list):
    """
    A class that inherits from the built-in list class.

    It includes a method to print the list in ascending sorted order.
    """

    def print_sorted(self):
        """
        Prints the list elements in ascending sorted order.
        """
        sorted_list = sorted(self)
        print(sorted_list)

if __name__ == "__main__":
    my_list = MyList([3, 1, 2])
    my_list.print_sorted()

    my_list = MyList([5, 7, 2, 4])
    my_list.print_sorted()

    my_list = MyList([10, 5])
    my_list.print_sorted()

    my_list = MyList([])
    my_list.print_sorted()
