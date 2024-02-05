#!/usr/bin/python3
import requests
from sys import argv

def main():
    r = requests.get(argv[1])
    status = r.status_code
    if status >= 400:
        print("Error code: {}".format(status))


if __name__ == '__main__':
    main()
