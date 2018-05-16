#!/usr/bin/python3
"""
module defines read_file
"""


def read_file(filename=""):
    """ reads file from text & prints to stdout
    args:
        filename (file): file to read
    """
    with open(filename, 'r', encoding='utf-8') as f:
        print(f.read())
