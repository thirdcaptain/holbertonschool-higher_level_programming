#!/usr/bin/python3
"""This module defines a square with errors"""


class Square:
    """This class defines a square, instatiated with size and position"""
    def __init__(self, size=0, position=(0, 0)):
        if (type(size) is not int):
            raise TypeError("size must be an integer")
        if (size < 0):
            raise ValueError("size must be >= 0")
        self.__size = size
        if type(position) is not tuple:
            raise TypeError("position must be a tuple of 2 positive integers")
        if len(position) is not 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        if not isinstance(position[0], int):
            raise TypeError("position must be a tuple of 2 positive integers")
        if not isinstance(position[1], int):
            raise TypeError("position must be a tuple of 2 positive integers")
        if position[0] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        if position[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        if len(position) > 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = position

    def area(self):
        """This method returns the area"""
        return self.__size * self.__size

    @property
    def size(self):
        """This getter returns the value for size"""
        return self.__size

    @size.setter
    def size(self, value):
        """This setter sets the value of size"""
        if (type(value) is not int):
            raise TypeError("size must be an integer")
        self.__size = value

    def my_print(self):
        """This method prints a square"""
        if self.__size == 0:
            print()
            return
        for vertical in range(self.__position[1]):
            print()
        else:
            for row in range(self.__size):
                for horizontal in range(self.__position[0]):
                    print(" ", end="")
                for column in range(self.__size):
                    print("#", end="")
                print()

    @property
    def position(self):
        """This getter returns the value for position"""
        return self.__position

    @position.setter
    def position(self, value):
        """This setter sets the value of position"""
        if (type(value) is not tuple):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value
