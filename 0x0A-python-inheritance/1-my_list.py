#!/usr/bin/python3


class MyList(list):
    """A class that inherits from list and provides a method to print the list in sorted order."""

    def print_sorted(self):
        """Prints the list in ascending order."""
        print(sorted(self))

if __name__ == "__main__":
    my_list = MyList([4, 2, 9, 1, 5, 6])
    my_list.print_sorted()
