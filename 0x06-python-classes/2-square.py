#!/usr/bin/python3
""" define a class named square """


class Square:
    """ defines a function named __init__ """
    def __init__(self, size=0):
        """ if statement """
        if type(size) is not int:
            """ raise an error """
            raise TypeError("size must be an integer")
        elif size < 0:
            """ raise an error """
            raise ValueError("size must be >= 0")
        else:
            """ initialize __size of self with size """
            self.__size = size
