#!/usr/bin/python3
"""  Python script that takes in a URL, sends
a request to the URL and displays the body
of the response (decoded in utf-8)
"""
import urllib.request
import urllib.error
from sys import argv


def main():
    """ main function """
    req = urllib.request.Request(argv[1])
    try:
        with urllib.request.urlopen(req) as response:
            page = response.read().decode('utf-8')
        print(page)
    except urllib.error.HTTPError as e:
        print("Error code: {}".format(e.code))


if __name__ == '__main__':
    main()
