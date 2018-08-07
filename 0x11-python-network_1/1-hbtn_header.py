#!/usr/bin/python3
"""Module displays X-Request-Id from header"""
if __name__ == "__main__":
    import urllib.request
    import sys
    with urllib.request.urlopen(sys.argv[1]) as response:
        header_dict = dict(response.info())
        print(header_dict.get('X-Request-Id'))
