#!/usr/bin/python3
"""Python script that takes in a URL, sends a request to the URL
and displays the value of the X-Request-Id variable
found in the header of the response.
"""
import urllib.request
import sys


def main():
    """ amin function """
    req = urllib.request.Request(sys.argv[1])
    with urllib.request.urlopen(req) as response:
        header = response.headers
    print(header['X-Request-Id'])


if __name__ == '__main__':
    main()
