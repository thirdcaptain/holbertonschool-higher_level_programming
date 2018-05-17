#!/usr/bin/python3
"""
module defines class BaseGeometry
"""


class BaseGeometry:
    """
    class defines baseGeometry
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
        if not type(value) is int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0"
                             .format(name))
