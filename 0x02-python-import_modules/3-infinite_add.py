#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    if len(sys.argv) == 1:
        print("0")
    elif len(sys.argv) == 2:
        num1 = int(sys.argv[1])
        print("{}".format(num1))
    else:
        num1 = int(sys.argv[1])
        num2 = int(sys.argv[2])
        print("{}".format(num1 + num2))
