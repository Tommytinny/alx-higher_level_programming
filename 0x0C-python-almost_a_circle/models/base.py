#!/usr/bin/python3
""" module for a base """
import json
import os
import csv
import turtle


class Base:
    """ implementing Base class """
    __nb_objects = 0

    def __init__(self, id=None):
        """
        init - intialization
        Args:
            id: Object id
        """
        if id is not None:
            self.id = id
        else:
            Base. __nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """
        JSON string representation of list_dictionaries
        Args:
            list_dictionaries: list of dictionary
        """
        if list_dictionaries is not None or list_dictionaries != []:
            return json.dumps(list_dictionaries)
        else:
            return "[]"

    @classmethod
    def save_to_file(cls, list_objs):
        """
        writes the JSON string representation of list_objs to a file
        Args:
            cls: name of class itself
            list_objs: list of instances who inherits of Base
        """
        filename = cls.__name__ + ".json"
        if list_objs is None or list_objs == []:
            lst = []
        else:
            lst = cls.to_json_string([i.to_dictionary() for i in list_objs])
        with open(filename, 'w') as f:
            f.write(lst)

        return lst

    @staticmethod
    def from_json_string(json_string):
        """
        returns the list of the JSON string representation json_string
        Args:
            json_string: string representing a list of dictionaries
        """
        if json_string is None or json_string == []:
            return []
        else:
            return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """
        returns an instance with all attributes already set
        Args:
            cls: class name itself
            dictionary: dictionaries
        """
        if cls.__name__ == "Rectangle":
            dummy = cls(1, 1)
        else:
            dummy = cls(1)

        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        """
        returns a list of instances
        Args:
            cls: class name itself
        """
        filename = cls.__name__ + ".json"
        lst = []
        if os.path.exists(filename):
            with open(filename, 'r') as f:
                s = f.read()
                list_dict = cls.from_json_string(s)
                for d in list_dict:
                    lst.append(cls.create(**d))
        return lst

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """
        serializes list_objs to a file in CSV
        Args:
            cls: class name itself
            list_objs: list of instances who inherits of Base
        """
        filename = cls.__name__ + ".csv"
        with open(filename, 'w') as csvfile:
            if list_objs is not None or list_objs != []:
                list_objs = [i.to_dictionary() for i in list_objs]
                if cls.__name__ == "Rectangle":
                    fields = ['id', 'width', 'height', 'x', 'y']
                elif cls.__name__ == "Square":
                    fields = ['id', 'size', 'x', 'y']
            csvwriter = csv.DictWriter(csvfile, fieldnames=fields)
            csvwriter.writeheader()
            csvwriter.writerows(list_objs)

    @classmethod
    def load_from_file_csv(cls):
        """
        deserializes list_objs to a file in CSV
        Args:
            cls: class name itself
            list_objs: list of instances who inherits of Base
        """
        filename = cls.__name__ + ".csv"
        lst = []
        if os.path.exists(filename):
            with open(filename, 'r') as csvfile:
                if cls.__name__ == "Rectangle":
                    fields = ['id', 'width', 'height', 'x', 'y']
                elif cls.__name__ == "Square":
                    fields = ['id', 'size', 'x', 'y']
                reader = csv.reader(csvfile, delimiter=',')
                for x, row in enumerate(reader):
                    if x > 0:
                        i = cls(1, 1)
                        for j, e in enumerate(row):
                            if e:
                                setattr(i, fields[j], int(e))
                        lst.append(i)
        return lst

    @staticmethod
    def draw(list_rectangles, list_squares):
        """
        opens a window and draws all the Rectangles and Squares
        Args:
            list_rectangles: lists of rectangle
            list_squares: list of square
        """
        screen = turtlr.Screen()
        pen = turtle.Pen()
        figures = list_rectangles + list_squares

        for fig in figures:
            pen.up()
            pen.goto(fig.x, fig.y)
            pen.down()
            pen.forward(fig.width)
            pen.right(90)
            pen.forward(fig.height)
            pen.right(90)
            pen.forward(fig.width)
            pen.right(90)
            pen.forward(fig.height)
            pen.right(90)

        window.exitonclick()
