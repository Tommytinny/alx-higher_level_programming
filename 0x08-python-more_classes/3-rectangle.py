#!/usr/bin/python3
"""
module for rectangle
"""


class Rectangle:
    """ rectangle """
    def __init__(self, width=0, height=0):
        """ initialize """
        self.__width = width
        self.__height = height

    @property
    def width(self):
        """ width getter """
        return self.__width

    @width.setter
    def width(self, value):
        """ width setter """
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """ height getter """
        return self.__height

    @height.setter
    def height(self, value):
        """ height setter """
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """ calculate area of a rectangle """
        return self.__height * self.__width

    def perimeter(self):
        """ calculate perimeter of rectangle """
        if self.__width == 0 or self.__height == 0:
            return 0
        else:
            return 2 * (self.__height + self.__width)

    def __str__(self):
        """ string representation of the rectangle """
        if self.__width == 0 or self.__height == 0:
            return ""
        else:
            hashes = ""
            height = self.__height
            while height != 0:
                if (height - 1) != 0:
                    hashes += "#" * self.__width + "\n"
                else:
                    hashes += "#" * self.__width
                height -= 1
            return hashes
