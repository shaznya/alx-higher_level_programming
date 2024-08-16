#!/usr/bin/python3
"""Writes a string to a text file (UTF8)."""


def write_file(filename="", text=""):
    """Writes a string to a text file (UTF8).

    Args:
        filename (str): The name of the file to write to.
        text (str): The text to write to the file. Defaults to an empty string.

    Returns:
        int: The number of characters written to the file.
    """
    with open(filename, 'w', encoding='utf-8') as file:
        return file.write(text)
