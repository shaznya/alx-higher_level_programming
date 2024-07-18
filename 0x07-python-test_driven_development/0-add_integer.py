#!/usr/bin/pyton3
def add_integer(a, b=98):
    """
    Function that adds two integers.
    
    Args:
        a (int or float): First number.
        b (int or float, optional): Second number. Defaults to 98.
        
    Returns:
        int: The integer sum of a and b.
        
    Raises:
        TypeError: If either a or b is not an integer or float.
                   Error message will be 'a must be an integer' or 'b must be an integer'.
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")

    return int(a) + int(b)

if __name__ == "__main__":
    import doctest
    doctest.testfile("tests/0-add_integer.txt")
