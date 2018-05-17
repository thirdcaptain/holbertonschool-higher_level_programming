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

    def to_json(self):
        """ retrieves dictionary representation of instance
        """
        return (self.__dict__)
