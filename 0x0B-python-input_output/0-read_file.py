#!/usr/bin/python3
"""Reads a UTF8 text file and prints its content to stdout."""


def read_file(filename=""):
    """Reads a text file (UTF8) and prints its content to stdout.

    Args:
        filename (str): The name of the file to read.
    """
    with open(filename, 'r', encoding='utf-8') as file:
        content = file.read()
        print(content, end='')


if __name__ == '__main__':
    pass
