#!/usr/bin/python3
"""Class definition"""
import json


class Base:
    """Definition of Base class"""

    __nb_objects = 0

    def __init__(self, id=None):

        """initializing instances

        Args:
            id (_type_, optional): _description_. Defaults to None.
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """Return the JSON representation of a string object."""
        if list_dictionaries is None:
            return "[]"
        else:
            return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """Writes the JSON string representation of list_objs to a file."""
        if list_objs is None:
            list_objs = []
        filename = cls.__name__ + ".json"
        with open(filename, "w") as file:
            lists = [obj.to_dictionary() for obj in list_objs]
            json_string = cls.to_json_string(lists)
            file.write(json_string)

    @staticmethod
    def from_json_string(json_string):
        """Returns the list of the JSON string representation"""
        if json_string is None or json_string == "":
            return "[]"
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """Returns an instance with attributes set from a dictionary."""
        if cls.__name__ == "Rectangle":
            dummy = cls(1, 1)
        elif cls.__name__ == "Square":
            dummy = cls(1)
        else:
            raise ValueError("Unsupported class for create method")

        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        """Returns a list of instances from a JSON file."""
        filename = cls.__name__ + ".json"
        try:
            with open(filename, "r") as file:
                json_string = file.read()
                json_data = json.loads(json_string)
                instances = [cls.create(**data) for data in json_data]
                return instances
        except FileNotFoundError:
            return []
