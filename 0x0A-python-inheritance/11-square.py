#!/usr/bin/python3
"""Square class Module"""
Rectangle = __import__("9-rectangle").Rectangle

class Rectangle(BaseGeometry):
    """
    A class representing a rectangle.
    """

    def __init__(self, width, height):
        """
        Initializes a Rectangle instance with the specified width and height.

        Args:
            width: The width of the rectangle (positive integer).
            height: The height of the rectangle (positive integer).
        """
        self.__width = width
        self.__height = height
        self.integer_validator("width", self.__width)
        self.integer_validator("height", self.__height)

    def area(self):
        """
        Calculates and returns the area of the rectangle.

        Returns:
            The area of the rectangle (width * height).
        """
        return self.__width * self.__height

    def __str__(self):
        """
        Returns a string representation of the Rectangle instance.
        """
        return "[Rectangle] {}/{}".format(self.__width, self.__height)
