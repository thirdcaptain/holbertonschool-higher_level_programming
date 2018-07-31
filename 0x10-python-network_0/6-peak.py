#!/usr/bin/python3
"""finds peak in a list of unsorted integers"""


def find_peak(list_of_integers):
    """returns a peak in a list"""
    if list_of_integers:
        # half = len(list_of_integers) // 2
        length = len(list_of_integers)
        for num in range(len(list_of_integers)):
            peak = list_of_integers[num]
            if length == 1:
                return peak
            if num == 0 and length == 2:
                if peak > list_of_integers[num + 1]:
                    return peak
                elif peak < list_of_integers[num + 1]:
                    return list_of_integers[num + 1]
                elif peak == list_of_integers[num + 1]:
                    return peak
            if num == 0 and length > 1:
                if list_of_integers[num + 1] < peak:
                    return peak
            elif num != length and length > 2:
                if (list_of_integers[num - 1] < peak and
                        list_of_integers[num + 1] < peak):
                    return peak
                if (list_of_integers[num - 1] == peak and
                        list_of_integers[num + 1] == peak):
                    return peak
            elif num == length:
                if (list_of_integers[num - 1] < peak):
                    return peak
    else:
        return None
