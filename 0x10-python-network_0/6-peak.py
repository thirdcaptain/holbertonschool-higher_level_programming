#!/usr/bin/python3
"""finds peak in a list of unsorted integers"""

def find_peak(list_of_integers):
    if list_of_integers:
        # half = len(list_of_integers) // 2
        for num in range(len(list_of_integers)):
            peak = list_of_integers[num]
            if num == 0 and len(list_of_integers) > 1:
                if list_of_integers[num + 1] < peak:
                    return peak
            elif num != len(list_of_integers):
                if (list_of_integers[num - 1] < peak and
                    list_of_integers[num + 1] < peak):
                    return peak
                if (list_of_integers[num - 1] == peak and
                    list_of_integers[num + 1] == peak):
                    return peak
            elif num == len(list_of_integers):
                if (list_of_integers[num - 1] < peak):
                    return peak
    else:
        return None
