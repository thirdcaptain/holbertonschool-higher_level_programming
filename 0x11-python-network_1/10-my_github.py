#!/usr/bin/python3
"""Queries the Github API"""
if __name__ == "__main__":
    import requests
    import sys
    url = 'https://api.github.com/user'
    user = sys.argv[1]
    password = sys.argv[2]
    page = requests.get(url, auth=(user, password))
    page_json = page.json()
    for key, value in page_json.items():
        if key == 'id':
            print(value)
