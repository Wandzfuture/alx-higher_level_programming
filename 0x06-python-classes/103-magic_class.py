#!/usr/bin/python3
"""Define a MagicClass that does the Python bytecode given by ALX"""
import math

class MagicClass:
    """Represent a circle."""

    def __init__(self, radius=0):
        """Initialize a MagicClass.

        Args:
            radius (float or int): The radius of the new MagicClass.
        Raises:
            TypeError: If radius is not a number (int or float).
        """
        self.__radius = 0
        if not isinstance(radius, (int, float)):
            raise TypeError("radius must be a number")
        self.__radius = radius

    def area(self):
        """Return the area of the MagicClass."""
        return (self.__radius**2 * math.pi)

    def circumference(self):
        """
        Return The circumference of the MagicClass.

        Returns:
            float: The circumference of the circle.
        """
        return (2 * math.pi * self.__radius)
