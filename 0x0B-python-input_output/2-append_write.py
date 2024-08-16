#!/usr/bin/python3
"""Appends a string at the end of a text file (UTF8)."""


def append_write(filename="", text=""):
    """Appends a string at the end of a text file (UTF8).

    Args:
        filename (str): The name of the file to append to.
        text (str): The text to append to the file.

    Returns:
        int: The number of characters added to the file.
    """
    with open(filename, 'a', encoding='utf-8') as file:
        num_characters = file.write(text)
    return num_characters


if __name__ == '__main__':
    pass
