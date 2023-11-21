#!/usr/bin/python3
""" square module """
from models.rectangle import Rectangle


class Square(Rectangle):
    """
    implementing square class
    """
    def __init__(self, size, x=0, y=0, id=None):
        """
        init - initialize
        Args:
            size: size of the square
            x: x position
            y: y position
            id: Object id
        """
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """
        overloading __str__ method
        """
        return "[Square] ({}) {}/{} - {}".format(
                self.id, self.x, self.y, self.height)

    @property
    def size(self):
        """ size getter """
        return self.height

    @size.setter
    def size(self, size):
        """ size setter """
        self.width = size
        self.height = size

    def update(self, *args, **kwargs):
        """ assigns an argument to each attribute """
        values = (self.id, self.size, self.x, self.y)
        if args:
            self.id, self.size, self.x, self.y =\
                    args + values[len(args):len(values)]
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        """
        dictionary representation of a Square
        """
        return {'id': self.id, 'x': self.x, 'size': self.size, 'y': self.y}
