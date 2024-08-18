#!/usr/bin/python3
"""Converts a Python object to a JSON string representation."""

import json

def to_json_string(my_obj):
    """Converts a Python object to a JSON string.

    Args:
        my_obj (object): The Python object to convert to JSON string.

    Returns:
        str: The JSON string representation of the object.
    """
    return json.dumps(my_obj)

if __name__ == '__main__':
    # Example usage
    sample_dict = {
        "name": "Alice",
        "age": 30,
        "city": "Wonderland",
        "is_student": False,
        "courses": ["Math", "Science"]
    }
    json_string = to_json_string(sample_dict)
    print("JSON representation:", json_string)
