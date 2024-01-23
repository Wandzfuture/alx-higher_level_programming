#!/usr/bin/python3
"""Define Python class MagicClass"""

import math

class MagicClass:
    """
    This class represents a MagicClass that calculates the area and circumference of a circle.

    Attributes:
    radius (float): The radius of the circle.

    Methods:
    area(): Calculates the area of the circle.
    circumference(): Calculates the circumference of the circle.
    """

    def __init__(self, radius):
        """
        Constructor for MagicClass.

        Args:
        radius (float): The radius of the circle.
        """
        self.__radius = 0
        if type(radius) is not int and type(radius) is not float:
            raise TypeError('radius must be a number')
        self.__radius = radius
    
    def area(self):
        """
        Calculates the area of the circle.

        Returns:
        float: The area of the circle.
        """
        return (self.__radius**2 * math.pi)
    
    def circumference(self):
        """
        Calculates the circumference of the circle.

        Returns:
        float: The circumference of the circle.
        """
        return (2 * math.pi * self.__radius)
