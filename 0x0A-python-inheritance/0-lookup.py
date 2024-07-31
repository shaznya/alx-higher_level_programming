#!/usr/bin/python3
def lookup(obj):
    """
    Returns a list of available attributes and methods of an object.

    Args:
        obj: The object to inspect.

    Returns:
        A list of strings representing the names of attributes and methods.
    """
    return dir(obj)

if __name__ == "__main__":
    class MyClass1:
        """A sample class for demonstration."""
        pass

    class MyClass2:
        """Another sample class with an attribute and a method."""
        my_attr1 = 3

        def my_meth(self):
            """A sample method."""
            pass
