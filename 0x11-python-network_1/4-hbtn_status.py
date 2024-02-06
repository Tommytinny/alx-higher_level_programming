#!/usr/bin/python3
"""Python script that fetches https://alx-intranet.hbtn.io/status
"""
import requests


def main():
    """ main function """
    r = requests.get('https://alx-intranet.hbtn.io/status')
    page = r.text
    print("Body response:")
    print("\t- type: {}".format(type(page)))
    print("\t- content: {}".format(page))


if __name__ == '__main__':
    main()
