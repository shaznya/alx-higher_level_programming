The `max_integer` function from `6-max_integer` module
=======================================================

Using `max_integer`
-------------------

Import the function:

    >>> max_integer = __import__('6-max_integer').max_integer

Typical cases:

    >>> max_integer([1, 2, 3, 4])
    4
    >>> max_integer([1, 3, 4, 2])
    4
    >>> max_integer([-1, -2, -3, -4])
    -1
    >>> max_integer([0, 0, 0, 0])
    0
    >>> max_integer([5])
    5

Empty list:

    >>> max_integer([])
    >>>

Floats:

    >>> max_integer([1.1, 2.2, 3.3])
    3.3

Mixed types:

    >>> max_integer([1, 2.2, 3])
    3

Single element:

    >>> max_integer([1])
    1
    >>> max_integer([1.5])
    1.5

Non-integer types:

    >>> max_integer([1, 'a', 3])
    Traceback (most recent call last):
        ...
    TypeError: list must be a list of integers or floats
