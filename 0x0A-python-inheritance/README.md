# MyList Project

This project defines a custom list class called `MyList` that inherits from the built-in Python `list` class. It adds a method to print the elements of the list in sorted order.

## Features

- Inherits from the built-in `list`.
- Contains a method `print_sorted` that prints the list in ascending order.

## Usage

To use the `MyList` class, create an instance of it and call the `print_sorted` method:

```python
from my_list import MyList

my_list = MyList([3, 1, 4, 1, 5, 9])
my_list.print_sorted()  # Output: [1, 1, 3, 4, 5, 9]
