#!/usr/bin/python3
"""
Defines a rectangle class
"""


class Rectangle:
    """
    Rectange Class
    """
    def __init__(self, width=0, height=0):
        """__init__ method that sets width and height of rectangle
        Args:
            width (int): width of rectangle
            height (int): height of rectangle
        """
        self.height = height
        self.width = width

    @property
    def width(self):
        """
        getter returns the value of width
        """
        return self.__width

    @width.setter
    def width(self, value):
        """ width setter for rectangle
        Args:
            value (int): width of rectangle
        Raises:
            TypeError: If value is not int.
            ValueError: If value is < 0.
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """
        getter returns the value of height
        """
        return self.__height

    @height.setter
    def height(self, value):
        """ sets the value of height
        Args:
            value (int): height of rectangle
        Raises:
            TypeError: If value is not int.
            ValueError: If value is < 0.
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """ Returns the area of the rectangle
        Return:
            Area of rectangle
        """
        return self.__width * self.__height

    def perimeter(self):
        """ Returns perimeter of the rectangle
        Return:
            Perimeter of rectangle
        """
        if self.__width <= 0 or self.__height <= 0:
            return 0
        return (self.__width * 2) + (self.__height * 2)

    def __str__(self):
        """
        __str__ method that returns a string rectagle using #
        """
        string = ""
        for row in range(self.__height):
            for column in range(self.__width):
                string += "#"
            if row != (self.__height - 1):
                string += "\n"
        return string
