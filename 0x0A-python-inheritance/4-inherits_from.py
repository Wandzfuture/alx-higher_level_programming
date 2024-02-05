#!/usr/bin/python3
"""Defines an inherited class-checking function.
"""


def inherits_from(obj, a_class):
    """Checks if the object is an inherited instance.

    Args:
        obj: Any object.
        a_class: A class to check against.

    Returns:
        True if obj is an instance of a class that inherited from a_class; False otherwise.
    """
    return issubclass(type(obj), a_class) and type(obj) is not a_class
