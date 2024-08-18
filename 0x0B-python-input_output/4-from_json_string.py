#!/usr/bin/python3
"""Converts a JSON string to a Python object."""

import json


def from_json_string(my_str):
    """Converts a JSON string to a Python object.

    Args:
        my_str (str): The JSON string to convert.

    Returns:
        object: The Python object represented by the JSON string.
    """
    return json.loads(my_str)


if __name__ == '__main__':
    # Example usage
    json_str = '{"name": "Alice", "age": 30, "city": "Wonderland"}'
    python_obj = from_json_string(json_str)
    print("Python object:", python_obj)
