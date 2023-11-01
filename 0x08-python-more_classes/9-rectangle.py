#!/usr/bin/python3
"""
Module that defines a rectangle
"""


class Rectangle:
    """ Represents a rectangle """

    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """ initialize """
        self.__width = width
        self.__height = height
        Rectangle.number_of_instances += 1

    def __str__(self):
        """ string representation of rectangle """
        if self.__width == 0 or self.__height == 0:
            return ''
        hashes = ""
        height = self.__height
        while height != 0:
            if (height - 1) != 0:
                hashes += str(self.print_symbol) * self.__width + "\n"
            else:
                hashes += str(self.print_symbol) * self.__width
            height -= 1
        return hashes

    def __del__(self):
        """ destructor """
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")

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
        return (self.__height * self.__width)

    def perimeter(self):
        """ calculate perimeter of a rectangle """
        if self.__width == 0 or self.__height == 0:
            return 0
        else:
            return (2 * (self.__height + self.__width))

    def __repr__(self):
        """ formal string representation of the rectangle """
        return "Rectangle({}, {})".format(self.__width, self.__height)

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """ statcic method """
        if type(rect_1) is not Rectangle:
            raise TypeError("rect_1 must be an instance of Rectangle")
        if type(rect_2) is not Rectangle:
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_1.area() > rect_2.area() or rect_1.area() == rect_2.area:
            return rect_1
        return rect_2

    @classmethod
    def square(cls, size=0):
        """ square """
        return cls(size, size)
