#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    if len(sys.argv) == 1:
        print("0")
    else:
        i = 1
        sum = 0
        while i < (len(sys.argv)):
            sum = sum + int(sys.argv[i])
            i += 1
        print("{}".format(sum))
