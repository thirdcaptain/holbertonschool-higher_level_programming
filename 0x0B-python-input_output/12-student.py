#!/usr/bin/python3
""" module defines class Student
"""


class Student:
    """ class Student
    """
    def __init__(self, first_name, last_name, age):
        """ initializes first_name, last_name, age
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """ retrieves dictionary representation of instance
            if name is in attrs, retrieve they key
            otherwise all attributes must be retrieved
        """
        if attrs is None:
            return (self.__dict__)
        else:
            new_dict = {}
            for key, value in self.__dict__.items():
                if key in attrs:
                    new_dict[key] = value
            return (new_dict)
