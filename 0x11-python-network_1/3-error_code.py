#!/usr/bin/python3
import urllib.request
import urllib.error
from sys import argv

def main():
    req = urllib.request.Request(argv[1])
    try:
        with urllib.request.urlopen(req) as response:
            page = response.read().decode('utf-8')
        print(page)
    except urllib.error.HTTPError as e:
        print("Error code: {}".format(e.code))
