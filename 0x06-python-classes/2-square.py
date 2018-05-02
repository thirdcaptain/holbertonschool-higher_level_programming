#!/usr/bin/python3
"""
This module defines a square with errors
"""


class Square:
    """
    This class defines a square with attribute size with exceptions
    """
    def __init__(self, size=0):
        if (type(size) is not int):
            raise TypeError("size must be an integer")
        if (size < 0):
            raise ValueError("size must be >= 0")
        self.__size = size
