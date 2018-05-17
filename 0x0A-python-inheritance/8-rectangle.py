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
