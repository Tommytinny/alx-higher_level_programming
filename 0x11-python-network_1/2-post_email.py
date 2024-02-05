#!/usr/bin/python3
import urllib.request
import urllib.parse
from sys import argv

def main():
    url = argv[1]
    values = {'email': argv[2]}
    data = urllib.encode('ascii')
    req = urllib.request.Request(url, data)
    with urllib.request.urlopen(req) as response:
        page = response.read()
    print(page)


if __name__ == '__main__':
    main()
