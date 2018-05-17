#!/usr/bin/python3
""" module defines class_to_json function
"""


def class_to_json(obj):
    """ returns the dictionary description with simple data structure
    args:
        obj (obj): object
    """
    return (obj.__dict__)
