#!/usr/bin/python3


class MyList(list):
    """
    A subclass of list that includes a method to print the list in ascending order.
    """

    def print_sorted(self):
        """
        Prints the list in ascending order.
        """
        sorted_list = self[:]
        sorted_list.sort()
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
