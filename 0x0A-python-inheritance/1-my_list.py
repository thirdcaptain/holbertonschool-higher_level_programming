#!/usr/bin/python3
"""
Module defines class MyList as subclass of list
"""


class MyList(list):
    """ defines class MyList
        subclass of list
    """
    def print_sorted(self):
        """
        prints a sorted list
        """
        sorted_list = list(self)
        sorted_list.sort()
        print(sorted_list)
