#!/usr/bin/python3
"""Creates a Python object from a JSON file."""

import json


def load_from_json_file(filename):
    """Creates a Python object from a JSON file.

    Args:
        filename (str): The name of the JSON file to read.

    Returns:
        object: The Python object represented by the JSON data in the file.
    """
    with open(filename, 'r', encoding='utf-8') as file:
        return json.load(file)


if __name__ == '__main__':
    # Example usage
    # Make sure to create a sample JSON file named
    try:
        obj = load_from_json_file('example.json')
        print("Loaded object:", obj)
    except FileNotFoundError:
        print("The file 'example.json' does not exist.")
