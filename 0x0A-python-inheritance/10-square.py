#!/usr/bin/python3
"""
module defines class BaseGeometry and Rectangle
"""

Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """
    class Square that is a subclass of Rectangle
    """
    def __init__(self, size):
        super().__init__(size, size)
        super().integer_validator("size", size)
        self.__size = size
