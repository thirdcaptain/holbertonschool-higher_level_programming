#!/usr/bin/python3
"""
module defines Base class
"""


class Base:
    """Base class
       tracks id
    """

    __nb_objects = 0

    def __init__(self, id=None):
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = type(self).__nb_objects
            """ type(self) == Base class"""
