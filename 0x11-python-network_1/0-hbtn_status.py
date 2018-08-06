#!/usr/bin/python3
"""module fetches https://intranet.hbtn.io/status"""
if __name__ == "__main__":
    import urllib.request
    with urllib.request.urlopen('https://intranet.hbtn.io/status') as response:
        html = response.read()
        html2 = html.decode("utf-8")
        print("Body response:")
        print("    - type: {}".format(type(html)))
        print("    - content: {}".format(html))
        print("    - utf8 content: {}".format(html2))
