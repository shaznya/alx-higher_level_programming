#!/usr/bin/python3

def to_json_string(my_obj):
    """
    Converts an object to its JSON string representation.

    Args:
        my_obj: The object to convert (e.g., list, dict, int, float, bool, str).

    Returns:
        A JSON string representation of the object.
    """
    if isinstance(my_obj, str):
        return '"' + my_obj.replace('"', '\\"') + '"'
    elif isinstance(my_obj, bool):
        return "true" if my_obj else "false"
    elif isinstance(my_obj, (int, float)):
        return str(my_obj)
    elif isinstance(my_obj, list):
        return '[' + ', '.join(to_json_string(e) for e in my_obj) + ']'
    elif isinstance(my_obj, dict):
        items = [
            f'{to_json_string(k)}: {to_json_string(v)}'
            for k, v in my_obj.items()
        ]
        return '{' + ', '.join(items) + '}'
    elif my_obj is None:
        return "null"
    else:
        raise TypeError(f"Object of type {type(my_obj).__name__} is not JSON serializable")

if __name__ == '__main__':
    import doctest
    doctest.testfile('tests/3-to_json_string.txt')
