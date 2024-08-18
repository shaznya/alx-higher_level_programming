#!/usr/bin/python3

def to_json_string(my_obj):
    """
    Convert a Python object to a JSON string representation.
    """
    if my_obj is None:
        return "null"
    elif isinstance(my_obj, bool):
        return "true" if my_obj else "false"
    elif isinstance(my_obj, int) or isinstance(my_obj, float):
        return str(my_obj)
    elif isinstance(my_obj, str):
        return '"' + my_obj.replace('"', '\\"') + '"'
    elif isinstance(my_obj, dict):
        items = []
        for key, value in my_obj.items():
            items.append(to_json_string(key) + ":" + to_json_string(value))
        return "{" + ",".join(items) + "}"
    elif isinstance(my_obj, list):
        items = [to_json_string(item) for item in my_obj]
        return "[" + ",".join(items) + "]"
    else:
        raise TypeError("Unsupported type")
