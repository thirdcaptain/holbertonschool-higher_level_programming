#!/usr/bin/python3
"""
module defines append_write function
"""


def append_write(filename="", text=""):
    """ appends text to a file
    args:
        filename (file): file to write to
        text (string): string to write
    """
    with open(filename, mode="a", encoding="utf-8") as f:
        return f.write(text)
