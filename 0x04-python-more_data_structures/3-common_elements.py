#!/usr/bin/python3
def common_elements(set_1, set_2):
    common = []
    for x in set_1:
        if x in set_2:
            common.append(x)
    common = set(common)
    return common