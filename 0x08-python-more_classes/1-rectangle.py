#!/usr/bin/python3

"""Defines a Rectangle class"""


class Rectangle:
    """Represent a Rectangle class"""

    def __init__(self, width=0, height=0):
        """
        Initialize a new instance of Rectangle

        Args:
            width (int): The width of the new rectangle
            height (int): The height of the new rectangle
        """
        self._width = width
        self._height = height

    @property
    def width(self):
        """The getter for the width"""
        return self._width

    @width.setter
    def width(self, value):
        """The width property setter for the rectangle class

        Args:
            value (int): The width to set

        Raises:
            TypeError: width must be an integer
            ValueError: with must be >= 0
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        self._width = value

    @property
    def height(self):
        """The getter for the rectangle height

        Returns:
            int: The height of the rectangle
        """
        return self._height

    @height.setter
    def height(self, value):
        """The height property setter for the rectangle class

        Args:
            value (int): The height to set

        Raises:
            TypeError: height must be an integer
            ValueError: height must be >= 0
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        self._height = value
