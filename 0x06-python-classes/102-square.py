#!/usr/bin/python3
"""Square that defines a square by: (based on 4-square.py)"""


class Square:
    """
    Represents a square with size attribute and methods for area calculation and comparison based on area.
    Attributes:
        __size (int or float): The size of the square.

    """
    def __init__(self, size=0):
        """Initializes a square with the given size.

        Args:
            size (int or float): The size of the square (default 0).
        Raises:
            TypeError: If size is not a number (int or float).
            ValueError: If size is less than 0.
        """
        self.size = size

    @property
    def size(self):
        """Getter method to retrieve the size of the square."""
        return (self.__size)

    @size.setter
    def size(self, value):
        """Setter method to set the size of the square.

        Args:
            value (int or float): The size of the square.
        Raises:
            TypeError: If value is not a number (int or float).
            ValueError: If value is less than 0.
        """
        if not isinstance(value, (int, float)):
            raise TypeError("size must be a number")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def area(self):
        """Calculates and returns the area of the square.

        Returns:
            float: The area of the square (size squared).
        """
        return (self.__size ** 2)

    def __eq__(self, other):
        """Checks if two squares are equal based on their areas.

        Args:
            other (Square): The square to compare with.
        Returns:
            bool: True if the areas are equal, False otherwise.
        """
        return (self.area() == other.area())

    def __ne__(self, other):
        """Checks if two squares are not equal based on their areas.

        Args:
            other (Square): The square to compare with.
        Returns:
            bool: True if the areas are not equal, False otherwise.
        """
        return (self.area() != other.area())

    def __lt__(self, other):
        """Checks if the area of the first square is less than the area of the second square.

        Args:
            other (Square): The square to compare with.
        Returns:
            bool: True if the area is less, False otherwise.
        """
        return (self.area() < other.area())

    def __le__(self, other):
        """Checks if the area of the first square is less than or equal to the area of the second square.

        Args:
            other (Square): The square to compare with.
        Returns:
            bool: True if the area is less or equal, False otherwise.
        """
        return (self.area() <= other.area())

    def __gt__(self, other):
        """Checks if the area of the first square is greater than the area of the second square.

        Args:
            other (Square): The square to compare with.
        Returns:
            bool: True if the area is greater, False otherwise.
        """
        return (self.area() > other.area())

    def __ge__(self, other):
        """Checks if the area of the first square is greater than or equal to the area of the second square.

        Args:
            other (Square): The square to compare with.
        Returns:
            bool: True if the area is greater or equal, False otherwise.
        """
        return (self.area() >= other.area())
