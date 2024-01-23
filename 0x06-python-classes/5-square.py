#!/usr/bin/python3
#5-square.py


class Square:
    """Represents a square with a size attribute and methods for area calculation and printing.

    Attributes:
        __size (int): The size of the square.

    Methods:
        __init__(self, size=0): Initializes a square with the given size.
        area(self): Calculates and returns the area of the square.
        size(self): Getter method to retrieve the size of the square.
        size(self, value): Setter method to set the size of the square.
        my_print(self): Prints the square using the '#' character.
    """

    def __init__(self, size=0):
        """Initializes a square with the given size.

        Args:
            size (int): The size of the square (default 0).
        Raises:
            TypeError: If size is not an integer.
            ValueError: If size is less than 0.
        """
        self.size = size

    @property
    def size(self):
        """Getter method to retrieve the size of the square."""
        return self.__size

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

    def area(self):
        """Calculates and returns the area of the square.

        Returns:
            int: The area of the square (size squared).
        """
        return self.__size ** 2

    def my_print(self):
        """Prints the square using the '#' character."""
        if self.__size == 0:
            print()
        else:
            for _ in range(self.__size):
                print("#" * self.__size)
