#!/usr/bin/python3
"""Queries the Star Wars API"""
if __name__ == "__main__":
    import requests
    import sys
    url = 'https://swapi.co/api/people/'
    try:
        term = sys.argv[1]
    except Exception:
        term = ""
    parameters = {'search': term}
    page = requests.get(url, params=parameters)
    json_dict = dict(page.json())
    json_count = json_dict.get('count')
    print("Number of results: {}".format(json_count))
    json_results = json_dict.get('results')
    for record in json_results:
        for key, value in record.items():
            if key == 'name':
                print(value)
