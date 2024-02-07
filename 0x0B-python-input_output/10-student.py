#!/usr/bin/python3
"""Defines a class Student."""


class Student:
    """Defines a student with first name, last name, and age."""

    def __init__(self, first_name, last_name, age):
        """Initializes a Student instance with the given attributes."""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        Returns a dictionary representation of the Student instance.

        Args:
            attrs (list, optional): List of attribute names to retrieve. If None, all attributes are retrieved.
        Returns:
            dict: A dictionary representation of the Student instance.
        """
        if attrs is None:
            return {
                "first_name": self.first_name,
                "last_name": self.last_name,
                "age": self.age
            }
        else:
            return {
                attr: getattr(self, attr)
                for attr in attrs
                if hasattr(self, attr)
            }
