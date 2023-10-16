#!/usr/bin/python3
"""Defines a Square class"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """Represent a square class"""
    def __init__(self, size, x=0, y=0, id=None):
        """Initializes a new square

        Args:
            size (int): Size of the square
            x (int, optional): x coordinate. Defaults to 0.
            y (int, optional): y coordinate. Defaults to 0.
            id (_type_, optional): object ID. Defaults to None.
        """
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """Overriding the __str__ method"""
        attributes = (self.id, self.x, self.y, self.width)
        return "[Square] ({}) {}/{} - {}".format(*attributes)

    @property
    def size(self):
        """Get the size value"""
        return (self.width)

    @size.setter
    def size(self, value):
        """Set the size value"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be > 0")
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """assigns an argument to each attribute"""
        default_values = [self.id, self.size, self.x, self.y]
        default_list = ["id", "size", "x", "y"]

        for i in range(min(len(default_values), len(args))):
            default_values[i] = args[i]

        for key, value in kwargs.items():
            if key in ("id", "size", "x", "y"):
                default_values[default_list.index(key)] = value

        self.id, self.size, self.x, self.y = default_values

    def to_dictionary(self):
        """Returns the dictionary representation of a Square"""
        return {
            'id': self.id,
            'size': self.size,
            'x': self.x,
            'y': self.y
        }
