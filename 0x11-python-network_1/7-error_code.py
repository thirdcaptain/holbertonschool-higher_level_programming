#!/usr/bin/python3
"""Requests a URL and handles error codes"""
if __name__ == "__main__":
    import requests
    import sys
    url = sys.argv[1]
    page = requests.get(url)
    if page.status_code == requests.codes.ok:
        print(page.text)
    else:
        print("Error code: {}".format(page.status_code))
