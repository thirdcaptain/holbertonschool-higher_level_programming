#!/usr/bin/python3
"""
module defines from_json_string function
"""


import json


def from_json_string(my_obj):
    """
    returns python object represented by JSON string
    args:
        my_obj (obj): json object
    """
    return json.loads(my_obj)
