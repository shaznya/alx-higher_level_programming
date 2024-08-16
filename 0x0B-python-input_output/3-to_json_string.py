#!/usr/bin/python3
import json


def to_json_string(my_obj):
    """
    Returns the JSON representation of an object (string).

    Args:
        my_obj (object): The object to be converted to JSON format.

    Returns:
        str: The JSON representation of the object.
    """
    return json.dumps(my_obj)
