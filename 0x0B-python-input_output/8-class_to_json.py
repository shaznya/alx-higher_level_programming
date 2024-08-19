#!/usr/bin/python3
"""Module that contains the class_to_json function."""


def class_to_json(obj):
    """Returns the dictionary description with simple data structure
    (list, dictionary, string, integer, and boolean) for JSON serialization.

    Args:
        obj: An instance of a Class.

    Returns:
        dict: A dictionary representation of the object.
    """
    return obj.__dict__


if __name__ == '__main__':
    class Student:
        def __init__(self, name, age, is_enrolled):
            self.name = name
            self.age = age
            self.is_enrolled = is_enrolled

    student = Student("Alice", 22, True)
    print(class_to_json(student))
