#!/usr/bin/python3
"""
module defines write_file function
"""


def write_file(filename="", text=""):
    """ writes text to a file
    args:
        filename (file): file to write to
        text (string): string to write
    """
    with open(filename, mode="w", encoding="utf-8") as f:
        return f.write(text)
