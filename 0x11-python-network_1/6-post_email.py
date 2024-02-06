#!/usr/bin/python3
"""Python script that takes in a URL and an email address
sends a POST request to the passed URL with the email as
a parameter, and finally displays the body of the response.
"""
import requests
from sys import argv

def main():
    """ main function """
    r = request.post(argv[1], data={'email': argv[2]})
    page = r.text
    print(page)


if __name__ == '__main__':
    main()
