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
    try:
        print(page_json['id'])
    except Exception:
        print("None")
