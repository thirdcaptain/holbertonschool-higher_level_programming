#!/usr/bin/python3
"""
Module defines lookup which returns attributes of an object
"""

def lookup(obj):
    """ returns attributes of an object
    parameters:
        obj (obj): object to determine parameters
    """
    return dir(obj)
