#!/usr/bin/python3
"""Defines a class square"""


class Square:
    """A class representing a square.
    Methods:
        __init__(self, size=0): Initializes a square with the given size.
        area(self): Calculates and returns the area of the square.
    """

    def __init__(self, size=0):
        """Initializes a square with the given size.
        """
        self.size = size

    @property
    def size(self):
        """Getter method to retrieve the size of the square.
        """
        return (self.__size)

    @size.setter
    def size(self, value):
        """Setter method to set the size of the square.
        """
        if type(value) is not int and type(value) is not float:
            raise TypeError('size must be a number')
        elif value < 0:
            raise ValueError('size must be >= 0')
        else:
            self.__size = value

    def area(self):
        """Calculates and returns the area of the square.

        Returns:
            The area of the square.
        """
        return self.__size ** 2

    def __lt__(self, other):
        """Checks if the area of the first square is less than the area of the second square.
        """
        return self.size < other.size

    def __le__(self, other):
        """Checks if the area of the first square is less than/equal to the area of the second square.

        Args:dd
            other (Square): The square to compare with.
        Returns:
            bool: True if the area is less or equal, False otherwise.
        """
        return self.size <= other.size

    def __eq__(self, other):
        """Checks if the area of the first square is equal to the area of the second square.
        """
        return self.size == other.size

    def __ne__(self, other):
        """Checks if the area of the first square is not equal to the area of the second square.
        """
        return self.size != other.size

    def __ge__(self, other):
        """Checks the area of the first square is greater than/equal to the second square.
        """
        return (self.size >= other.size)
