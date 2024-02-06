#!/usr/bin/python3
"""list 10 commits (from the most recent to oldest)
of the repository “rails” by the user “rails”
Print all commits by: `<sha>: <author name>` (one by line)
"""
import requests
import sys


def main():
    """ main function """
    repo = sys.argv[1]
    owner = sys.argv[2]
    token = "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"
    header = {'Authorization': f'Bearer {token}'}
    url = f"https://api.github.com/repos/{owner}/{repo}/commits"
    r = requests.get(url, headers=header)
    page = r.json()
    if r.status_code == 200:
        count = 1
        for key in page:
            name = key['commit']['author']['name']
            sha = key['sha']
            if count <= 10:
                print("{}: {}".format(sha, name))
            count += 1


if __name__ == '__main__':
    main()
