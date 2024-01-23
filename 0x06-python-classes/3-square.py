#!/usr/bin/python3
"""Represents a square with a size attribute and methods for area calculation."""

class Square:
    """ class Square that defines a square"""

    def __init__(self, size=0):
        """initialize square
        Args:
            size (int): size of the square
        """
        if type(size) is not int:
            raise TypeError('size must be an integer')
        elif size < 0:
            raise ValueError('size must be >= 0')
        else:
            self.__size = size  #: size of the square

    def area(self):
        """returns the area.

        Returns:
            ares.
        """
        return self.__size**2
