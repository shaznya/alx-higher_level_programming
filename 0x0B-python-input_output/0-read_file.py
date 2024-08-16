#!/usr/bin/python3

def read_file(filename=""):
    """
    Reads a text file (UTF8) and prints it to stdout.

    Args:
        filename (str): The path to the file to be read. Defaults to an empty string.
    """
    with open(filename, 'r', encoding='utf-8') as file:
        # Read and print the content of the file
        print(file.read(), end='')
