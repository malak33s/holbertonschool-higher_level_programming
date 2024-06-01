#!/usr/bin/env python3
"""Learn pickle module"""
import pickle


class CustomObject:
    def __init__(self, name, age, is_student):
        """Initialize a CustomObject"""
        self.name = name
        self.age = age
        self.is_student = is_student

    def display(self):
        """Display CustomObject"""
        print("Name: {}".format(self.name))
        print("Age: {}".format(self.age))
        print("Is Student: {}".format(self.is_student))

    def serialize(self, filename):
        """Serialize CustomObject"""
        try:
            with open(filename, 'wb') as f:
                pickle.dump(self, f)
        except (FileNotFoundError, pickle.PickleError):
            return None

    @classmethod
    def deserialize(cls, filename):
        """Deserialize CustomObject"""
        try:
            with open(filename, 'rb') as f:
                return pickle.load(f)
        except (FileNotFoundError, pickle.PickleError):
            return None
