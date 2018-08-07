#!/usr/bin/python3
"""Requests a URL with a POST request and email parameter"""
if __name__ == "__main__":
    import requests
    import sys
    url = sys.argv[1]
    address = sys.argv[2]
    parameters = {'email': address}
    page = requests.post(url, data=parameters)
    print(page.text)
