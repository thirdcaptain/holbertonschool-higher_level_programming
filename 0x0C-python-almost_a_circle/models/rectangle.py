#!/usr/bin/python3
"""
module defines rectangle class
"""


from models.base import Base

class Rectangle(Base):
    """
    class defines Rectangle:
    args:
        width (int): width
        height (int): height
        x (int): x
        y (int): y
    """
    def __init__(self, width, height, x=0, y=0, id=None):
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

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
            """
            self.__width = value

        @property
        def height(self):
            """
            getter returns the value of height
            """
            return self.__height

        @height.setter
        def height(self, value):
            """height setter for rectangle
            Args:
                value (int): height of rectangle
            """
            self.__height = value

        @property
        def x(self):
            """
            getter returns the value of x
            """
            return self.__x

        @x.setter
        def x(self,value):
            """x setter for rectangle
            Args:
                value (int): x of rectangle
            """
            self.__x = value

        @property
        def y(self):
            """
            getter returns the value of y
            """
            return self.__y

        @y.setter
        def y(self,value):
            """y setter for rectangle
            Args:
                value (int): y of rectangle
            """
            self.__y = value
