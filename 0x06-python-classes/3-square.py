#!/usr/bin/python3
"""Represents a square with a size attribute and methods for area calculation."""


class Square:
    """
    Class that defines properties of a square.

    Attributes:
        __size (int): size of a square (1 side).
    """

    def __init__(self, size=0):
        """
        Initialize new instances of square.

        Args:
            size (int, optional): size of the square (1 side).
                Defaults to 0.

        Raises:
            TypeError: If size is not an integer.
            ValueError: If size is less than 0.
        """
        self.__size = size

        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")

    def area(self):
        """
        Calculates the area of the square.

        Returns:
            int: The current square area.
        """
        return self.__size ** 2
