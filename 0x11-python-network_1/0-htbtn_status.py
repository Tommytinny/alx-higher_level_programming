#!/usr/bin/python3
"""Python script that fetches https://alx-intranet.hbtn.io/status
"""
import utllib.request

def main():
    """ main function """
    req = urllib.request.Request('https://alx-intranet.hbtn.io/status')
    with urllib.request.urlopen(req) as response:
        page = response.read()
        print("Body response:\n\t- type: {}\n\t- content: {}\n\t- utf8 content: {}"\
                .format(type(page), page, page.decode('utf-8')))

if __name__ == '__main__':
    main()