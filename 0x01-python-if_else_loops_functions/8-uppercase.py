#!/usr/bin/python3
def uppercase(str):
    for c in str:
        if ord(c) in range(ord('a'), ord('z') + 1):
            d = chr(ord(c) - 32)
        else:
            d = c
        print("{}".format(d), end="")
    print("")
