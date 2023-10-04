#!/usr/bin/env python3
def uppercase(str):
    for char in str:
        if 'a' <= char <= 'z':
            uppercase = chr(ord(char) - ord('a') + ord('A'))
        else:
            uppercase = char
        print("{}".format(uppercase), end='')
    print()
