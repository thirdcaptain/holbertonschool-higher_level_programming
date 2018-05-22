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
        if list_dictionaries is None:
            list_dictionaries = []
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        list_objects = []
        filename = str(cls.__name__) + ".json"
        if not any(list_objs):
            with open(filename, mode="w", encoding="utf-8") as f:
                f.write(cls.to_json_string(list_objects))
        else:
            for obj in list_objs:
                list_objects.append(cls.to_dictionary(obj))
            with open(filename, mode="w", encoding="utf-8") as f:
                f.write(cls.to_json_string(list_objects))
