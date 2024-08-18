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

    def reload_from_json(self, json):
        """Replaces all attributes of the Student instance.

        Args:
            json (dict): A dictionary representing the new attributes and their values.
        """
        for key, value in json.items():
            setattr(self, key, value)


# Example usage
if __name__ == '__main__':
    student = Student("John", "Doe", 21)
    
    # Printing initial state
    print(student.to_json())  # Prints all attributes

    # Reload from a JSON dictionary
    new_data = {"first_name": "Jane", "last_name": "Smith", "age": 22}
    student.reload_from_json(new_data)
    
    # Printing updated state
    print(student.to_json())
