#!/usr/bin/python3
"""Python script that takes in a URL, sends a request
to the URL and displays the body of the response.
"""
import requests
from sys import argv


def main():
    """ amin function """
    r = requests.get(argv[1])
    status = r.status_code
    if status >= 400:
        print("Error code: {}".format(status))
    else:
        print(r.text)


if __name__ == '__main__':
    main()
