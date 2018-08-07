#!/usr/bin/python3
"""Module displays X-Request-Id from header"""
if __name__ == "__main__":
    import urllib.request
    import sys
    with urllib.request.urlopen(sys.argv[1]) as response:
        html = response.read()
    print(response.info().get_all('X-Request-Id')[0])
