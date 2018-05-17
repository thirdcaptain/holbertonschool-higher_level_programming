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
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def __str__(self):
        """
        __str__ method that prints square description
        """
        string = "[Square] " + str(self.__size) + "/" + str(self.__size)
        return string
