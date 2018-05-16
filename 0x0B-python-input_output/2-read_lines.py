#!/usr/bin/python3
"""
Module defines read_lines function
"""


def read_lines(filename="", nb_lines=0):
    """
    reads lines of text
    args:
        filename (file): file to read from
        nb_lines (int): number of lines to read
            reads entire file if <= 0 or >= # of lines
    """
    linenumber = 0
    count = 0
    with open(filename, encoding='utf-8') as f:
        for line in f:
            linenumber += 1
    if nb_lines <= 0 or nb_lines >= linenumber:
        with open(filename, encoding='utf-8') as f:
            for line in f:
                print(line, end="")
    else:
        with open(filename, encoding='utf-8') as f:
            for line in f:
                print(line, end="")
                count += 1
                if count == nb_lines:
                    return
