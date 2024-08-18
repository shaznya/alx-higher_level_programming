#!/usr/bin/python3
"""Defines a Student class."""


class Student:
    """Represents a student with first name, last name, and age."""
    
    def __init__(self, first_name, last_name, age):
        """Initializes a new Student instance.

        Args:
            first_name (str): The first name of the student.
            last_name (str): The last name of the student.
            age (int): The age of the student.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Retrieves a dictionary representation of a Student instance.

        Args:
            attrs (list, optional): A list of attribute names to retrieve. Defaults to None.

        Returns:
            dict: A dictionary containing the specified attributes, or all attributes if attrs is None.
        """
        if attrs is None:
            return self.__dict__
        else:
            return {key: value for key, value in self.__dict__.items() if key in attrs}


# Example usage
if __name__ == '__main__':
    student = Student("John", "Doe", 21)
    print(student.to_json())
    print(student.to_json(["first_name", "age"]))
