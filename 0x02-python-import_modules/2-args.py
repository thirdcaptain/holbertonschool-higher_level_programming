#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    len = len(sys.argv)
    list = sys.argv
    if len == 1:
        print("0 arguments.")
    elif len == 2:
        print("1 argument:")
        print("1: {}".format(sys.argv[1]))
    else:
        print("{} arguments:".format(len - 1))
        index = 0
        for i in list:
            if index != 0:
                print("{}: {}".format(index, i))
            index += 1
