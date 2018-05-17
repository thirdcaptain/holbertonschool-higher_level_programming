#!/usr/bin/python3
"""
module defines class BaseGeometry and Rectangle
"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


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
