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
        self.width = width
        self.height = height

    @property
    def width(self):
        """The getter for the width"""
        return self.__width

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
        self.__width = value

    @property
    def height(self):
        """The getter for the rectangle height

        Returns:
            int: The height of the rectangle
        """
        return self.__height

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
        self.__height = value

    def area(self):
        """Returns the area of the rectangle

        Returns:
            int: The area of the rectangle
        """
        return (self.width * self.height)

    def perimeter(self):
        """Return the perimeter of the rectangle

        Returns:
            int: Returns the perimeter of the rectangle
        """
        if self.width == 0 or self.height == 0:
            return 0
        return (self.width + self.height) * 2
