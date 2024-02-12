#!/usr/bin/python3
"""Defines a square class."""
from models.rectangle import Rectangle


class Square(Rectangle):
    """Represent a square with a size attribute.

    Inherits from Rectangle class with width and height set
    to the size attribute.
    """

    def __init__(self, size, x=0, y=0, id=None):
        """Initialize a new Square.

        Args:
            size (int): The size of the new Square.
            x (int): The x coordinate of the new Square.
            y (int): The y coordinate of the new Square.
            id (int): The identity of the new Square.

        Raises:
            TypeError: If size is not an integer.
            ValueError: If size is less than or equal to 0.
        """
        if not isinstance(size, int) or size <= 0:
            raise TypeError("size must be an integer greater than 0")
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """Get/set the size of the Square."""
        return self.width

    @size.setter
    def size(self, value):
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """Update the Square attributes.

        Args:
            *args (ints): New attribute values.
                - 1st argument represents id attribute
                - 2nd argument represents size attribute
                - 3rd argument represents x attribute
                - 4th argument represents y attribute
            **kwargs (dict): New key/value pairs of attributes.
        """
        if args and len(args) != 0:
            if len(args) == 1:
                if isinstance(args[0], int):
                    self.__init__(self.size, self.x, self.y, args[0])
                else:
                    raise TypeError("id must be an integer")
            elif len(args) == 4:
                self.__init__(args[1], args[2], args[3], args[0])
            else:
                raise TypeError("update takes 1 positional argument "
                                "or keyword arguments")

        elif kwargs and len(kwargs) != 0:
            for k, v in kwargs.items():
                if k == "id":
                    if isinstance(v, int):
                        self.id = v
                    else:
                        raise TypeError("id must be an integer")
                elif k == "size":
                    if not isinstance(v, int) or v <= 0:
                        raise TypeError("size must be an integer greater "
                                        "than 0")
                    self.size = v
                elif k in ["x", "y"]:
                    if not isinstance(v, int) or v < 0:
                        raise ValueError("{} must be an integer greater "
                                         "than or equal to 0".format(k))
                    setattr(self, k, v)
                else:
                    raise TypeError("{} is not a valid attribute".format(k))

    def to_dictionary(self):
        """Return the dictionary representation of the Square."""
        return {
            "id": self.id,
            "size": self.width,
            "x": self.x,
            "y": self.y
        }

    def __str__(self):
        """Return the print() and str() representation of a Square."""
        return "[Square] ({}) {}/{} - {}".format(self.id, self.x, self.y,
                                                 self.width)
