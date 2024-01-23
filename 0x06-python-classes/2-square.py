#!/usr/bin/python3
"""Class that defines a square."""


class Square:
    """
    Class that defines properties of square by: (based on 1-square.py).

    Attributes:
        size: size of a square (1 side).
    """

    def __init__(self, size=0):
        """Creates new instances of square.

        Args:
            size: size of the square (1 side).
        Raises:
            TypeError: If size is not an integer.
            ValueError: If size is less than 0.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    @property
    def size(self):
        """Getter method for the size attribute."""
        return (self.__size)

    @size.setter
    def size(self, value):
        """Setter method for the size attribute.

        Args:
            value (int): The new size value.
        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value
