#!/usr/bin/python3
def to_json_string(my_obj):
    """
    Returns the JSON string representation of an object (string).
    
    Args:
        my_obj (object): The object to convert to JSON string.
    
    Returns:
        str: JSON string representation of the object.
    """
    # Manually constructing the JSON string without using any imports
    if isinstance(my_obj, dict):
        items = []
        for key, value in my_obj.items():
            items.append(f'"{key}": {to_json_string(value)}')
        return '{' + ', '.join(items) + '}'
    elif isinstance(my_obj, list):
        items = [to_json_string(item) for item in my_obj]
        return '[' + ', '.join(items) + ']'
    elif isinstance(my_obj, str):
        return f'"{my_obj}"'
    elif isinstance(my_obj, bool):
        return 'true' if my_obj else 'false'
    elif isinstance(my_obj, (int, float)):
        return str(my_obj)
    else:
        raise TypeError(f"Object of type {type(my_obj).__name__} is not JSON serializable")

if __name__ == '__main__':
    # Test the function with some examples
    my_list = [1, 2, 3]
    print(to_json_string(my_list))

    my_dict = { 
        'id': 12,
        'name': "John",
        'places': ["San Francisco", "Tokyo"],
        'is_active': True,
        'info': {
            'age': 36,
            'average': 3.14
        }
    }
    print(to_json_string(my_dict))

    try:
        my_set = {132, 3}
        print(to_json_string(my_set))
    except Exception as e:
        print("[{}] {}".format(e.__class__.__name__, e))
