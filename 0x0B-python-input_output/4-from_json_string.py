#!/usr/bin/python3
import json

def from_json_string(my_str):
    """
    Returns an object (Python data structure) represented by a JSON string.

    Args:
        my_str (str): The JSON string to be converted into a Python object.

    Returns:
        object: A Python data structure corresponding to the JSON string.
    """
    return json.loads(my_str)
