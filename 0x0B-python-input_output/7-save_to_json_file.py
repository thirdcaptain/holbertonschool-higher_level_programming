#!/usr/bin/python3
"""
module defines save_to_json_file
"""


import json
def save_to_json_file(my_obj, filename):
    """ function writes object to text
    args:
        my_obj (obj): object to write to text file
        filename (file): file to write to
    """
    with open(filename, mode="w", encoding="utf-8") as f:
        return f.write(json.dumps(my_obj))
