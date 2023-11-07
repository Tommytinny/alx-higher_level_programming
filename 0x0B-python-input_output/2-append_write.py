#!/usr/bin/python3
"""
append_write
"""


def append_write(filename="", text=""):
    """
    append_write - function that appends a string at the end of a
                    text file (UTF8) and returns the number of characters added
    Args:
        filename: name of the file
        text: text to be written
    Return: number of bytes written.
    """
    with open(filename, 'a', encoding="utf-8") as f:
        return (f.write(text))
