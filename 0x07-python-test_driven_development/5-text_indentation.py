#!/usr/bin/python3
"""
Defines a function that parses and prints text with two new lines after:
period, question mark, and colon
"""

def text_indentation(text):

    if not isinstance(text, str):
        raise TypeError("text must be a string")

    character = ['.', ':', '?']

    new_text = ""
    for n in text:
        if n not in character:
            new_text += n
        else:
            new_text += n + "\n\n"

#    new_text = "".join(n if n not in character
#                       else n + "\n\n" for n in text)
#    print(new_text)

    new_list = []
    temp_list = new_text.split("\n")
    for i in temp_list:
        new_list.append(i.strip())
    print("\n".join(new_list), end="")

#    if not isinstance(text, str):
#        raise TypeError("text must be a string")
#    length = len(text)
#    i = 0
#    while i < length:
#        while text[i] == ' ':
#            i += 1
#            if i >= (length - 1):
#                break
#        while (i < length and text[i] != '.' and text[i] != '?' and text[i] != ':'):
#            print("{}".format(text[i]),end="")
#            i += 1
#            if i >= (length - 1):
#                break
#        if i == (length - 1):
#            print("{}".format(text[i]))
#        else:
#            print("{}\n".format(text[i]))
#        i += 1
#        if i >= (length - 1):
#            break
