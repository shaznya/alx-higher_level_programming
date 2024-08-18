#!/usr/bin/python3
"""Writes a Python object to a text file as JSON."""

import json


def save_to_json_file(my_obj, filename):
    """Writes a Python object to a text file as JSON.

    Args:
        my_obj (object): The Python object to write to the file.
        filename (str): The name of the file to write the JSON data to.
    """
    with open(filename, 'w', encoding='utf-8') as file:
        json.dump(my_obj, file)


if __name__ == '__main__':
    # Example usage
    data = {
        "name": "Alice",
        "age": 30,
        "city": "Wonderland",
        "is_student": False,
        "courses": ["Math", "Science"]
    }
    save_to_json_file(data, 'data.json')
    print("Data has been written to 'data.json'.")
