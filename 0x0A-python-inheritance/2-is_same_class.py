#!/usr/bin/python3
"""Defines a class-checking function.
"""


def is_same_class(obj, a_class):
    """
    Checks if the object is exactly an instance of the specified class.

    Args:
        obj: Any object.
        a_class: A class to compare against.

    Returns:
        True if obj is an instance of a_class; False otherwise.
    """
    return type(obj) is a_class
