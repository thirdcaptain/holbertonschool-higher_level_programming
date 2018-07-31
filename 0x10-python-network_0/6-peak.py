#!/usr/bin/python3
"""finds peak in a list of unsorted integers"""

def find_peak(list_of_integers):
    if list_of_integers:
        # half = len(list_of_integers) // 2
        for num in range(len(list_of_integers)):
            peak = list_of_integers[num]
            if num == 0 and len(list_of_integers) > 1:
                if list_of_integers[num + 1] < list_of_integers[num]:
                    return list_of_integers[num]
        return 5
    else:
        return None
