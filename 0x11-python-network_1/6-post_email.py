#!/usr/bin/python3
import requests
from sys import argv

def main():
    r = request.post(argv[1], data={'email': argv[2]})
    page = r.text
    print(page)


if __name__ == '__main__':
    main()
