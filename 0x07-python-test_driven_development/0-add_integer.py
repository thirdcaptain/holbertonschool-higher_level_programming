#!/usr/bin/python3
"""
Defines a function that sum of two integers
"""


def add_integer(a, b=98):
    """
    Adds the sum of two integers
    """
    if type(a) is float:
        a = int(a)
    if type(b) is float:
        b = int(b)
    if type(a) is not int:
        raise TypeError("a must be an integer")
    if type(b) is not int:
        raise TypeError("b must be an integer")
    if a is None:
        raise TypeError("a must be an integer")
    if b is None:
        raise TypeError("b must be an integer")
    return a + b
