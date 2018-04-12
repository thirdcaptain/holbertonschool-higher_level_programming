#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    if len(sys.argv) < 3:
        print("0")
    else:
        num1 = int(sys.argv[1])
        num2 = int(sys.argv[2])
        print("{}".format(num1 + num2))
