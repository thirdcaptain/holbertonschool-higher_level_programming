#!/usr/bin/python3
"""
Defines a rectangle class
"""


class Rectangle:
    """
    Rectange Class
    """

    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """__init__ method that sets width and height of rectangle
        Args:
            width (int): width of rectangle
            height (int): height of rectangle
        """
        self.height = height
        self.width = width
        type(self).number_of_instances += 1

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
                string += str(self.print_symbol)
            if row != (self.__height - 1):
                string += "\n"
        return string

    def __repr__(self):
        """
        __repr__ method that recreates a new instance
        """
        return ("Rectangle(" + str(self.__width) + ", " +
                str(self.__height) + ")")

    def __del__(self):
        """
        prints Bye rectangle... when instance is deleted
        also decrements counter when instance is deleted
        """
        print("Bye rectangle...")
        type(self).number_of_instances -= 1

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """
        returns the biggest rectangle based on area
        """
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_1.area() >= rect_2.area():
            return rect_1
        return rect_2

    @classmethod
    def square(cls, size=0):
        """
        Returns a new Rectangle instance of width == height == size
        """
        if size < 0:
            raise ValueError("size must be >= 0")
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        return cls(size, size)
