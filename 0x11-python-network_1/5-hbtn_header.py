#!/usr/bin/python3
"""Fetches X-Request-Id using requests module"""
if __name__ == "__main__":
    import requests
    import sys
    url = sys.argv[1]
    page = requests.get(url)
    print(page.headers.get('X-Request-Id'))
