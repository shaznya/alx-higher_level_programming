#!/usr/bin/python3
"""Student class with JSON serialization and deserialization methods."""


class Student:
    """Defines a student by first_name, last_name, and age."""

    def __init__(self, first_name, last_name, age):
        """Initializes a Student instance with given attributes."""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Retrieves a dictionary representation of the Student instance.

        Args:
            attrs (list): Optional list of attribute names to retrieve.

        Returns:
            dict: Dictionary representation of the Student instance.
        """
        if attrs is None:
            return self.__dict__

        if isinstance(attrs, list):
            return {k: getattr(self, k) for k in attrs if hasattr(self, k)}

        return {}

    def reload_from_json(self, json):
        """Replaces all attributes of the Student instance.

        Args:
            json (dict): Dictionary containing attribute names and values.
        """
        if isinstance(json, dict):
            for key, value in json.items():
                setattr(self, key, value)


if __name__ == "__main__":
    student = Student("John", "Doe", 25)
    print("Initial student:", student.to_json())

    student_json = student.to_json(["first_name", "age"])
    print("Student JSON with selected attributes:", student_json)

    student.reload_from_json({"first_name": "Jane", "age": 30})
    print("Updated student:", student.to_json())
