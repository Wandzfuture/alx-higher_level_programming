#!/usr/bin/python3
"""Empty class Square that defines a square."""


class Square:
    """
    Class that defines properties of square by: (based on 0-square.py).

    Attributes:
        size: size of a square (1 side).
    """

    def __init__(self, size=0):
        """Initialize the square with a given size.

        Args:
            size (int): The size of the square.
        """
        self.__size = size
