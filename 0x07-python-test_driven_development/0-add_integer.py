#!/usr/bin/python3
"""Defines an integer addition function."""


def add_integer(a, b=98):
    """
    Function to add 2 integers.

    :param a: int or float
    :param b: int or float
    :return: int
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer or b must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer or b must be an integer")

    a = int(a)
    b = int(b)

    return (a + b)
