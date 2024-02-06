#!/usr/bin/python3
"""Python script that takes in a letter and sends a POST request to
http://0.0.0.0:5000/search_user with the letter as a parameter.
"""
import requests
from sys import argv


def main():
    """ main fuction """
    if len(argv) > 1:
        q = argv[1]
    else:
        q = ""
    try:
        r = requests.post('http://0.0.0.0:5000/search_user', data={'q': q})
        page = r.json()
        if bool(page):
            print("[{}] {}".format(page['id'], page['name']))
        else:
            print("No result")
    except ValueError as e:
        print("Not a valid JSON")


if __name__ == '__main__':
    main()
