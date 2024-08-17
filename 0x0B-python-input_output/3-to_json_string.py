#!/usr/bin/python3
import json


def to_json_string(my_obj):
    """
    Returns the JSON representation of an object (string).

    Args:
        my_obj: The object to convert to JSON.

    Returns:
        A JSON string representation of the object.
    """
    return json.dumps(my_obj)
