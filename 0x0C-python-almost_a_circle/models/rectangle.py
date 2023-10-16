#!/usr/bin/python3
"""Defines a rectangle class"""
from models.base import Base


class Rectangle(Base):
    """Represent a rectangle class"""
    def __init__(self, width, height, x=0, y=0, id=None):
        """Initializes a new rectangle

        Args:
            width (int): Set the rectangle width
            height (int): Set the rectangle heigth
            x (int, optional): _description_. Defaults to 0.
            y (int, optional): _description_. Defaults to 0.
            id (_type_, optional): _description_. Defaults to None.
        """
        if type(width) is not int:
            raise TypeError("width must be an integer")
        elif width < 0:
            raise ValueError("width must be > 0")
        self.__width = width

        if type(height) is not int:
            raise TypeError("height must be an integer")
        elif height < 0:
            raise ValueError("height must be > 0")
        self.__height = height

        if type(x) is not int:
            raise TypeError("x must be an integer")
        elif x < 0:
            raise ValueError("x must be >= 0")
        self.__x = x

        if type(y) is not int:
            raise TypeError("y must be an integer")
        elif y < 0:
            raise ValueError("y must be >= 0")
        self.__y = y

        super().__init__(id)

    @property
    def width(self):
        """Get the width value"""
        return (self.__width)

    @width.setter
    def width(self, value):
        """Set the width value"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """Get the height value"""
        return (self.__height)

    @height.setter
    def height(self, value):
        """Set the height value"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """Get x value"""
        return (self.__x)

    @x.setter
    def x(self, value):
        """Set the x value"""
        if not isinstance(value, int):
            raise TypeError("x must be an integer")
        elif value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """Get the y value"""
        return (self.__y)

    @y.setter
    def y(self, value):
        """Set the y value"""
        if not isinstance(value, int):
            raise TypeError("y must be an integer")
        elif value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """Returns the area value of the Rectangle instance"""
        return (self.__width * self.__height)

    def display(self):
        """Prints in stdout the Rectangle instance with the character #"""
        for _ in range(self.y):
            print()
        for row in range(self.__height):
            spaces = " " * self.x
            hashes = "#" * self.__width
            print(spaces + hashes)

    def __str__(self):
        """Overriding the __str__ method"""
        attributes = (self.id, self.x, self.y, self.__width, self.__height)
        return ("[Rectangle] ({}) {}/{} - {}/{}".format(*attributes))

    def update(self, *args, **kwargs):
        """assigns an argument to each attribute"""
        default_values = [self.id, self.__width, self.__height, self.x, self.y]
        default_list = ["id", "width", "height", "x", "y"]

        for i in range(min(len(args), len(default_values))):
            default_values[i] = args[i]

        for key, value in kwargs.items():
            if key in ("id", "width", "height", "x", "y"):
                default_values[default_list.index(key)] = value

        self.id, self.__width, self.__height, self.x, self.y = default_values
    
    def to_dictionary(self):
        """Returns the dictionary representation of a Rectangle"""
        return {
            'id': self.id,
            'width': self.width,
            'height': self.height,
            'x': self.x,
            'y': self.y
        }
