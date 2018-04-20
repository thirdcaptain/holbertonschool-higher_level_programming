#!/usr/bin/python3
def roman_to_int(roman_string):
    num = 0
    list = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    if roman_string:
        for i in reversed(roman_string):
            if i in list:
                num += list[i]
            else:
                return 0
        return num
    else:
        return 0
