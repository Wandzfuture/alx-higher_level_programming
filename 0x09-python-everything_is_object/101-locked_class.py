#!/usr/bin/python3
""" Module for `LockedClass`
"""

class LockedClass:
    """Prevents dynamic creation of new instance attributes except 'first_name'."""
    def __setattr__(self, name, value):
        """Prevent dynamic creation of new instance attributes except 'first_name'."""
        if name != "first_name":
            raise AttributeError("'LockedClass' object has no attribute '{}'".format(name))
        super().__setattr__(name, value)
