#!/usr/bin/python3
import json

def to_json_string(my_obj):
    """
    Returns the JSON string representation of an object (string).
    
    Args:
        my_obj (object): The object to convert to JSON string.
    
    Returns:
        str: JSON string representation of the object.
    """
    return json.dumps(my_obj)

