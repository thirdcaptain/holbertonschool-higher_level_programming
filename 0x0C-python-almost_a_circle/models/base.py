#!/usr/bin/python3
"""
module defines Base class
"""


import json


class Base:
    """Base class
       tracks id
    """

    __nb_objects = 0

    def __init__(self, id=None):
        """Initializer method
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = type(self).__nb_objects
            """ type(self) == Base class"""

    @staticmethod
    def to_json_string(list_dictionaries):
        """ returns JSON string
        args:
            list_dictionaries (list): list of dictionaries
        """
        if not any(list_dictionaries):
            return "[]"
        else:
            return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        
