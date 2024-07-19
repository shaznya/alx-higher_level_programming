def add_integer(a, b=98):
    """
    Adds two integers.
    
    Args:
        a: The first number.
        b: The second number, default is 98.
    
    Returns:
        The integer sum of the two numbers.
    
    Raises:
        TypeError: If `a` or `b` is not an integer or float.
    """
    if type(a) not in [int, float]:
        raise TypeError("a must be an integer")
    if type(b) not in [int, float]:
        raise TypeError("b must be an integer")
    
    return int(a) + int(b)
