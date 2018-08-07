#!/usr/bin/python3
"""Fetches website information using requests module"""
if __name__ == "__main__":
    import requests
    page = requests.get('https://intranet.hbtn.io/status')
    print("Body response:")
    print("\t- type: {}".format(type(page.text)))
    print("\t- content: {}".format(page.text))
