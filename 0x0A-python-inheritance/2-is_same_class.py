#!/usr/bin/python3
"""
module defines is_same_class function that returns True if object is a class
"""


def is_same_class(obj, a_class):
    """ determines if a obj is an exact instance of a_class
    Args:
        obj (object): object to evaluate
        a_class(class): class to evaluate

    Returns:
        True returns True if object is an instance of a class
        False if otherwise
    """
    if type(obj) == a_class:
        return True
    else:
        return False
