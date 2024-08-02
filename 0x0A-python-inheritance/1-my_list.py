#!/usr/bin/python3

class MyList(list):
    """
    A class that inherits from the built-in list and includes
    a method to print the list in ascending order.
    """

    def print_sorted(self):
        """
        Prints the list in ascending sorted order.
        Assumes that all elements in the list are integers.
        """
        sorted_list = self[:]
        for i in range(len(sorted_list)):
            for j in range(i + 1, len(sorted_list)):
                if sorted_list[i] > sorted_list[j]:
                    sorted_list[i], sorted_list[j] = sorted_list[j], sorted_list[i]
        print(sorted_list)
