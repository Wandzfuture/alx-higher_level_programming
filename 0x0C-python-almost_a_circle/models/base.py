#!/usr/bin/python3
"""
Defines the Base class for all other classes in this project.
"""

class Base:
    """
    The Base class manages the id attributes in classes
    """

    __nb_objects = 0

    def __init__(self, id=None):
        """
        Initialize the Base object.

	assigns id it to the public instance attribute id.
        Otherwise, increment __nb_objects and assign the new value
	to the public instance attribute id.
        """
        if id is not None:
            self.id = id
        else:
            self.id = Base.__nb_objects + 1
            Base.__nb_objects += 1

    @classmethod
    def create(cls, **dictionary):
        """
        Return an instance with all attributes already set.

        **dictionary can be thought of as a double pointer to a dictionary
        To use the update method to assign all attributes, create a "dummy"
	instance before:
        Call update instance method to this "dummy" instance.
        **dictionary must be used as **kwargs of the method update
        """
        dummy = cls(0, 0, 0)
        dummy.update(**dictionary)
        return dummy

    @classmethod
    def save_to_file(cls, list_objs):
        """
        Write the JSON representation of list_objs to a file.

        If list_objs is None, save an empty list.
        The filename must be: <Class name>.json - example: Rectangle.json
        Overwrite the file if it already exists.
        """
        filename = f"{cls.__name__}.json"
        list_dicts = [obj.to_dictionary() for obj in list_objs]
        json_string = cls.to_json_string(list_dicts)
        with open(filename, "w") as file:
            file.write(json_string)

    @classmethod
    def load_from_file(cls):
        """
        Return a list of instances from a JSON file.
        """
        filename = f"{cls.__name__}.json"
        try:
            with open(filename, "r") as file:
                json_string = file.read()
                list_dicts = cls.from_json_string(json_string)
                return [cls.create(**d) for d in list_dicts]
        except FileNotFoundError:
            return []

    @staticmethod
    def to_json_string(list_dictionaries):
        """
        Return the JSON string representation of list_dictionaries.

        If list_dictionaries is None or empty, return the string: "[]".
        Otherwise, return JSON string representation of list_dictionaries.
        """
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        else:
            return json.dumps(list_dictionaries)

    @staticmethod
    def from_json_string(json_string):
        """
        Return a list of dictionaries from a JSON string.
        """
        if json_string is None or len(json_string) == 0:
            return []
        else:
            return json.loads(json_string)

    def to_dictionary(self):
        """
        Return a dictionary representation of the instance.
        """
        dictionary = self.__dict__.copy()
        dictionary.update({"id": self.id})
        return dictionary

    def update(self, *args, **kwargs):
        """
        Update the instance with new keyword arguments.

        If any argument is not a keyword argument, it is ignored.
        """
        for key, value in kwargs.items():
            if key in self.__class__.__dict__:
                setattr(self, key, value)
