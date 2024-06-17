#!/usr/bin/python3
"""Defines a Node and SinglyLinkedList classes."""


class Node:
    """A class representing a node in a singly linked list."""

    def __init__(self, data, next_node=None):
        """Initialize a node with data and optional reference to next node.

        Args:
            data: The data to be stored in the node.
            next_node (Node, optional): Reference to the next node.
        """
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """Get the data stored in the node."""
        return self.__data

    @data.setter
    def data(self, value):
        """Set the data in the node.

        Args:
            value: The value to be set as data.

        Raises:
            TypeError: If the value is not an integer.
        """
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        self.__data = value

    @property
    def next_node(self):
        """Get the reference to the next node."""
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        """Set the reference to the next node.

        Args:
            value (Node or None): The next node or None.

        Raises:
            TypeError: If the value is not a Node or None.
        """
        if not isinstance(value, (Node, type(None))):
            raise TypeError("next_node must be a Node object")
        self.__next_node = value


class SinglyLinkedList:
    """A class representing a singly linked list."""

    def __init__(self):
        """Initialize an empty singly linked list with a head set to None."""
        self.head = None

    def sorted_insert(self, value):
        """Insert a new Node into the correct sorted position in the list.

        Args:
            value: The value to be inserted into the list.
        """
        new_node = Node(value)
        if self.head is None or self.head.data >= value:
            new_node.next_node = self.head
            self.head = new_node
        else:
            current = self.head
            while (current.next_node is not None and
                   current.next_node.data < value):
                current = current.next_node
            new_node.next_node = current.next_node
            current.next_node = new_node

    def __str__(self):
        """Return a string representation of the linked list."""
        current = self.head
        result = []
        while current is not None:
            result.append(str(current.data))
            current = current.next_node
        return '\n'.join(result)


# Example usage
if __name__ == "__main__":
    ll = SinglyLinkedList()
    ll.sorted_insert(5)
    ll.sorted_insert(3)
    ll.sorted_insert(10)
    ll.sorted_insert(1)
    print(ll)
