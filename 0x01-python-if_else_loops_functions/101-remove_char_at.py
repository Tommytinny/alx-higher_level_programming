#!/usr/bin/python3
def remove_char_at(str, n):
    string = ""
    count = 0
    for i in str:
        if n == count:
            string += ""
        else:
            string += i
        count += 1
    return string
