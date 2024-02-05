#!/usr/bin/python3
import urllib.request
import sys

def main():
    req = urllib.request.Request(sysargv[1])
    with urllib.request.urlopen(req) as response:
        header = response.headers
    print(headers['X-Request-Id'])


if __name__ == '__main__':
    main()
