#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    sorted_dict = sorted(a_dictionary)
    for i in sorted_dict:
        print("{name}: {val}".format(name=i, val=a_dictionary[i]))
