#!/usr/bin/python3
"""class Student with methods for JSON serialization & deserialization."""


class Student:
    """Represents a student."""

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
        """Retrieves a dictionary representation of the Student instance.

        If attrs is a list of strings, only the attributes with names in
        this list will be retrieved.

        Args:
            attrs (list): A list of attribute names to include in the result.

        Returns:
            dict: A dictionary containing the requested attributes.
        """
        if isinstance(attrs, list) and all(isinstance(attr, str) for attr in attrs):
            return {
                attr: getattr(self, attr)
                for attr in attrs if hasattr(self, attr)
            }
        return self.__dict__

    def reload_from_json(self, json):
        """Replaces all attributes of the Student instance with those in the given dictionary.

        Args:
            json (dict): A dictionary containing the new attributes.
        """
        for key, value in json.items():
            setattr(self, key, value)
