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
