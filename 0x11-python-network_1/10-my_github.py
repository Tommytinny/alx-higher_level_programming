#!/usr/bin/python3
"""Python script that takes your GitHub credentials
(username and password) and uses the GitHub API to display your id
ou must use Basic Authentication with a personal access token as
password to access to your information (only read:user permission is needed)
"""
import requests
from sys import argv


def main():
    """ main fuction """
    username = argv[1]
    headers = {'Authorization': f'Bearer {argv[2]}'}
    r = requests.get('https://api.github.com/user', headers=headers)
    page = r.json()
    try:
        print(page['id'])
    except KeyError as e:
        print("None")


if __name__ == '__main__':
    main()
