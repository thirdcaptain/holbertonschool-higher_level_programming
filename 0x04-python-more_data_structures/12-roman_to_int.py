#!/usr/bin/python3
def roman_to_int(roman_string):
    num = 0
    list = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    if type(roman_string) == str:
        prev = 0
        for i in roman_string:
            if i in list:
                if list[i] > prev:
                    num -= prev * 2
                num += list[i]
                prev = list[i]
            else:
                return 0
        return num
    else:
        return 0
