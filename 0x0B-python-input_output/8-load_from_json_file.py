#!/usr/bin/python3
"""
module defines load_from_json_file
"""


import json


def load_from_json_file(filename):
    """
    creates an object from a JSON file
    args:
        filename (file): file to load object from
    """
    text = ""
    with open(filename, mode="r", encoding="utf-8") as f:
        for line in f:
            text += line
        return json.loads(text)
