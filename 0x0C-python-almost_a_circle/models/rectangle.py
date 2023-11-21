#!/usr/bin/python3
""" module that defines a Rectangle """
from models.base import Base


class Rectangle(Base):
    """ implementation of Rectangle """

    def __init__(self, width, height, x=0, y=0, id=None):
        """
        init - initialize
        Args:
            width: width of rectangle
            height: height of rectangle
            x: x position
            y: y position
            id: object id
        """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    def valid(self, char, value, equals=True):
        """
        validate for type and value error
        """
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(char))
        if equals:
            if value <= 0:
                raise ValueError("{} must be > 0".format(char))
        else:
            if value < 0:
                raise ValueError("{} must be >= 0".format(char))

    def __str__(self):
        """ overriding __str__ method """
        return "[Rectangle] ({}) {}/{} - {}/{}".format(
                self.id, self.x, self.y, self.width, self.height)

    @property
    def width(self):
        """ width getter """
        return self.__width

    @width.setter
    def width(self, width):
        """ width setter """
        self.valid('width', width)
        self.__width = width

    @property
    def height(self):
        """ height getter """
        return self.__height

    @height.setter
    def height(self, height):
        """ height setter """
        self.valid('height', height)
        self.__height = height

    @property
    def x(self):
        """ x getter """
        return self.__x

    @x.setter
    def x(self, x):
        """ x setter """
        self.valid('x', x, False)
        self.__x = x

    @property
    def y(self):
        """ y getter """
        return self.__y

    @y.setter
    def y(self, y):
        """ y setter """
        self.valid('y', y, False)
        self.__y = y

    def area(self):
        """ calculate area of rectangle """
        return self.__height * self.__width

    def display(self):
        height = self.height
        for y in range(self.y):
            print()
        while height != 0:
            for x in range(self.x):
                print(" ", end='')
            for i in range(self.width):
                print("#", end='')
            print()
            height -= 1

    def update(self, *args, **kwargs):
        """ assigns an argument to each attribute """
        values = (self.id, self.width, self.height, self.x, self.y)
        if args:
            self.id, self.width, self.height, self.x, self.y \
                    = args + values[len(args):len(values)]
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        """
        dictionary representation of a Rectangle
        """
        return {'x': self.x, 'y': self.y, 'id': self.id,
                'height': self.height, 'width': self.width}
