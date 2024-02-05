#!/usr/bin/python3
import requests

def main():
    r = requests.get('https://alx-intranet.hbtn.io/status')
    page = r.text
    print("Body response:\n\t- type: {}\n\t- content: {}"
            .format(type(page), page))


if __name__ == '__main__':
    main()
