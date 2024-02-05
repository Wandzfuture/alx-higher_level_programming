#!/usr/bin/python3
"""A module to prints a list in ascending order
"""

class MyList(list):
    """
    A custom list class that inherits from the built-in list class.
    """

    def print_sorted(self):
        """Prints a list in ascending order."""

        if issubclass(MyList, list):
            print(sorted(self))
