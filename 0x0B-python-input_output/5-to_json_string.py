#!/usr/bin/python3
"""
module defines to_json_string function
"""


import json
def to_json_string(my_obj):
    """
    returns the JSON string representation of an object
    args:
        my_obj (obj): json object
    """
    return json.dumps(my_obj)
