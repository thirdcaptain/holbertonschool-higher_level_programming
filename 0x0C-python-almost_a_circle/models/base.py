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

    @classmethod
    def reset(cls):
        """resets __nb_objects
        """
        cls.__nb_objects = 0

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
        """Saves JSON string representation to file
        args:
            list_objs (list): list of instances that inherit from Base
        """
        list_objects = []
        filename = str(cls.__name__) + ".json"
        if list_objs is None:
            with open(filename, mode="w", encoding="utf-8") as f:
                f.write(cls.to_json_string(list_objects))
        else:
            for obj in list_objs:
                list_objects.append(cls.to_dictionary(obj))
            with open(filename, mode="w", encoding="utf-8") as f:
                f.write(cls.to_json_string(list_objects))

    @staticmethod
    def from_json_string(json_string):
        """returns the list of the JSON string representation
        args:
            json_string (str): list of dictionaries
        """
        list_json = []
        if json_string is None:
            return list_json
        if not any(json_string):
            return list_json
        else:
            list_json = json.loads(json_string)
            return(list_json)

    @classmethod
    def create(cls, **dictionary):
        """returns an instance with all attributes already set
        args:
            **dictionary (dict): description of attributes
        """
        if cls.__name__ == "Square":
            tmp_cls = cls(1)
        elif cls.__name__ == "Rectangle":
            tmp_cls = cls(1, 1)
        tmp_cls.update(**dictionary)
        return tmp_cls

    @classmethod
    def load_from_file(cls):
        """returns a list of instances
        """
        text = ""
        json_list = []
        instance_list = []
        filename = str(cls.__name__) + ".json"
        try:
            with open(filename, mode="r", encoding="utf-8") as f:
                for line in f:
                    text += line
            json_list = cls.from_json_string(text)
            for element in json_list:
                instance_list.append(cls.create(**element))
            return instance_list
        except FileNotFoundError:
            return json_list
