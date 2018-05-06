#!/usr/bin/python3
"""
Defines a function that parses and prints text with two new lines after:
period, question mark, and colon
"""

def text_indentation(text):
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    length = len(text)
    i = 0
    while i < length:
        while text[i] == ' ':
            i += 1
            if i >= (length - 1):
                break
        while (i < length and text[i] != '.' and text[i] != '?' and text[i] != ':'):
            print("{}".format(text[i]),end="")
            i += 1
            if i >= (length - 1):
                break
        print("{}\n".format(text[i]))
        i += 1
        if i >= (length - 1):
            break
