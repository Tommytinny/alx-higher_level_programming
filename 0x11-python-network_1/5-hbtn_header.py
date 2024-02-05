#!/usr/bin/python3
import requests
from sys import argv

def main():
    r = requests.get(argv[1])
    page = r.headers['X-Request-Id']
    print(page)


if __name__ == '__main__':
    main()
