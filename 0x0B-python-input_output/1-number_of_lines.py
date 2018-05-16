#!/usr/bin/python3
"""
module defines number_of_lines function
"""


def number_of_lines(filename=""):
    """ returns the number of lines of a text file
    args:
        filename (file): file to read
    """
    linenumber = 0
    with open(filename, 'r', encoding='utf-8') as f:
        for line in f:
            linenumber += 1
    return linenumber
