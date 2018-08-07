#!/usr/bin/python3
"""POST request to site with a letter as a parameter"""
if __name__ == "__main__":
    import requests
    import sys
    url = 'http://0.0.0.0:5000/search_user'
    try:
        letter = sys.argv[1]
    except Exception:
        letter = ""
    parameters = {'q': letter}
    page = requests.post(url, data=parameters)
    try:
        results = page.json()
        if 'id' in results:
            json_id = results.get('id')
            json_name = results.get('name')
            print("[{}] {}".format(json_id, json_name))
        else:
            print("No result")
    except Exception:
        print("Not a valid JSON")
