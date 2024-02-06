#!/usr/bin/python3
"""Python script that takes in a URL, sends a request 
to the URL and displays the value of the variable
X-Request-Id in the response header"""
import requests
from sys import argv

def main():
    """ main function """
    r = requests.get(argv[1])
    page = r.headers['X-Request-Id']
    print(page)


if __name__ == '__main__':
    main()
