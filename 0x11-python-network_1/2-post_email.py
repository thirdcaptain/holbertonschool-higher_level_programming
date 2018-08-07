#!/usr/bin/python3
"""Module sends POST request to URL and displays body of response"""
if __name__ == "__main__":
    import urllib.request
    import sys
    import urllib.parse
    url = sys.argv[1]
    values = {'email': sys.argv[2]}
    data = urllib.parse.urlencode(values)
    data = data.encode('utf-8')
    req = urllib.request.Request(url, data)
    with urllib.request.urlopen(req) as response:
        the_page = response.read()
        print(the_page.decode("utf-8"))
