#!/usr/bin/python3
"""Defines a class Square"""


class Square:
    """
    Represent a square with size and position attributes and methods for area calculation and printing.

    Attributes:
        __size (int): The size of the square.
        __position (tuple): The position of the square.

    Methods:
        __init__(self, size=0, position=(0, 0)): Initializes a square with the given size and position.
        area(self): Calculates and returns the area of the square.
        size(self): Getter method to retrieve the size of the square.
        size(self, value): Setter method to set the size of the square.
        position(self): Getter method to retrieve the position of the square.
        position(self, value): Setter method to set the position of the square.
        my_print(self): Prints the square with the character '#' according to its size and position.
        __str__(self): Returns a string representation of the square for printing.

    """

    def __init__(self, size=0, position=(0, 0)):
        """Initializes a square with the given size and position.

        Args:
            size (int): The size of the square (default 0).
            position (tuple): The position of the square (default (0, 0)).
        Raises:
            TypeError: If size is not an integer or position is not a tuple of 2 positive integers.
            ValueError: If size is less than 0 or position contains non-positive integers.
        """
        self.size = size
        self.position = position

    @property
    def size(self):
        """Getter method to retrieve the size of the square."""
        return (self.__size)

    @size.setter
    def size(self, value):
        """Setter method to set the size of the square.

        Args:
            value (int): The size of the square.
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

    @property
    def position(self):
        """Getter method to retrieve the position of the square."""
        return (self.__position)

    @position.setter
    def position(self, value):
        """Setter method to set the position of the square.

        Args:
            value (tuple): The position of the square.
        Raises:
            TypeError: If value is not a tuple of 2 positive integers.
            ValueError: If value does not contain 2 positive integers.
        """
        if not isinstance(value, tuple) or len(value) != 2 or not all(isinstance(i, int) for i in value) or not all(i >= 0 for i in value):
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = value

    def area(self):
        """Calculates and returns the area of the square.

        Returns:
            int: The area of the square (size squared).
        """
        return (self.__size ** 2)

    def my_print(self):
        """Prints the square with the character '#' according to its size and position."""
        if self.__size == 0:
            print()
        else:
            for _ in range(self.__position[1]):
                print()
            for _ in range(self.__size):
                print(" " * self.__position[0] + "#" * self.__size)

    def __str__(self):
        """Returns a string representation of the square for printing."""
        if self.__size == 0:
            return ("")
        else:
            result = ""
            for _ in range(self.__position[1]):
                result += "\n"
            for _ in range(self.__size):
                result += " " * self.__position[0] + "#" * self.__size + "\n"
            return (result.rstrip())
