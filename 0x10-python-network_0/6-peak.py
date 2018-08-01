#!/usr/bin/python3
"""finds peak in a list of unsorted integers"""


def find_peak(list_of_integers):
    """returns a peak in a list"""
    if list_of_integers:
        # half = len(list_of_integers) // 2
        length = len(list_of_integers)
        peak = list_of_integers[0]
        for num in list_of_integers:
            if length == 1:
                return peak
            if num > peak:
                peak = num
        return peak
    else:
        return None
