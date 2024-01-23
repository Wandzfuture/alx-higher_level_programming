#!/usr/bin/python3
import math
#103-magic_class.py


class MagicClass:
    def __init__(self, radius):
        """
        Initialize a new MagicClass object with the given radius.

        Args:
            radius (number): The radius of the MagicClass object. Must be a number.

        Raises:
            TypeError: If radius is not a number.

        """
        if type(radius) is not int and type(radius) is not float:
            raise TypeError('radius must be a number')
        self._MagicClass__radius = 0
        self._MagicClass__radius = radius

    def area(self):
        """
        Return the area of the MagicClass object.

        """
        return (pow(self._MagicClass__radius, 2) * math.pi)

    def circumference(self):
        """
        Return the circumference of the MagicClass object.

        """
        return (2 * math.pi * self._MagicClass__radius)
