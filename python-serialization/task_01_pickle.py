#!/usr/bin/python3
"""Define serialization and deserialization pickle"""
import pickle


class CustomObject:
    """Define class CustomObject"""
    def __init__(self, name, age, is_student):
        """"Initialize CustomObject

        Args:
            name (str): name of the object
            age (int): age of the object
            is_student (bool): is the object a student
        """
        self.name = name
        self.age = age
        self.is_student = is_student

    def display(self):
        """Define methode to print object's attributes"""
        print("Name: {}".format(self.name))
        print("Age: {}".format(self.age))
        print("Is student: {}".format(self.is_student))

    def serialize(self, filename):
        """Define method to serialize object"""
        try:
            with open(filename, 'wb') as f:
                pickle.dump(self, f)
        except (FileNotFoundError, Exception):
            return None

    @classmethod
    def deserialize(cls, filename):
        """Define methode to deserialize object"""
        try:
            with open(filename, 'rb') as f:
                return pickle.load(f)
        except (FileNotFoundError, Exception):
            return None
