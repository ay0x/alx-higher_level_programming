#!/usr/bin/python3

"""Defines an empty class"""


class BaseGeometry:
    """Represents a geometry"""
    def area(self):
        """Raise Exception"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        self.name = name
        if not isinstance(value, int):
            raise TypeError(f"{name} must be an integer")
        elif value <= 0:
            raise ValueError(f"{name} must be greater than 0")
        else:
            setattr(self, name, value)