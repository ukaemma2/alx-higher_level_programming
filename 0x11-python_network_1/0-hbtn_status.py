#!/usr/bin/env python3

# A Python script that fetches https://alx-intranet.hbtn.io/status
import urllib.request

url = 'https://alx-intranet.hbtn.io/status'

try:
    with urllib.request.urlopen(url) as res:
        content = res.read()

    print("Body respond:")
    print("\t- type: {}".format(type(content)))
    print("\t- content: {}".format(content))
    print("\t- utf-8 content: {}".format(content.decode('utf-8')))

except urllib.error.URLError as e:
    print("Error: {}".format(e))
