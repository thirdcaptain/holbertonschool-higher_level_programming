#!/usr/bin/python3
"""
module defines class BaseGeometry and Rectangle
"""


class BaseGeometry:
    """
    class defines BaseGeometry
    """
    def area(self):
        """
        public instance method
        raises an exception
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        public instance method
        validates value
        """
        if not isinstance(value, int):
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0"
                             .format(name))


class Rectangle(BaseGeometry):
    """
    class Rectangle that is subclass of BaseGeometry
    """
    def __init__(self, width, height):
        """
        initializes width and height, validating with integer_validator
        """
        super().integer_validator("width", width)
        super().integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """ Returns the area of the rectangle
        Return:
            Area of rectangle
        """
        return self.__width * self.__height

    def __str__(self):
        """
        __str__ method that prints rectangle description
        """
        string = "[Rectangle] " + str(self.__width) + "/" + str(self.__height)
        return string


class Square(Rectangle):
    """
    class Square that is a subclass of Rectangle
    """
    def __init__(self, size):
        super().__init__(size, size)
        super().integer_validator("size", size)
        self.__size = size

    def __str__(self):
        """
        __str__ method that prints square description
        """
        string = "[Square] " + str(self.__size) + "/" + str(self.__size)
        return string
