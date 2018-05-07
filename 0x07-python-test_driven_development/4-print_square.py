#!/usr/bin/python3
"""
Defines a function that prints a square with #
"""


def print_square(size):
    """
    prints a square with #
    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    if size == 0:
        return
    for row in range(size):
        for column in range(size):
            print("#", end="")
        print()
