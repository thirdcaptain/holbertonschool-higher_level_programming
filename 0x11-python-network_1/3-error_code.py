#!/usr/bin/python3
"""Module sends POST request to URL and displays body of response"""
if __name__ == "__main__":
    import urllib.request
    import sys
    import urllib.error

    url = sys.argv[1]
    try:
        with urllib.request.urlopen(url) as req:
            print(req.read().decode('utf-8'))
    except urllib.error.HTTPError as e:
        print('Error code: {}'.format(e.code))
