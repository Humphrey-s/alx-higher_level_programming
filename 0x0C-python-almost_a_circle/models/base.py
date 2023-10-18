#!/usr/bin/python3
"""Definition Base class."""
import json


class Base:
    """Base Class."""
    __nb_objects = 0

    def __init__(self, id=None):

        if id is not None:

            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """convert to json string"""
        if list_dictionaries is None:
            return "[]"

        s = json.dumps(list_dictionaries)

        return s

    @classmethod
    def save_to_file(cls, list_objs):
        """convert to json and store in a file"""

        file = cls.__name__ + ".json"

        with open(file, "w", encoding="utf-8") as f:

            if list_objs is None:

                f.write("[]")

            else:

                p = [i.to_dictionary() for i in list_objs]

                f.write(Base.to_json_string(p))

    @staticmethod
    def from_json_string(json_string):
        """converts json string to python list"""
        if json_string is None:

            return []
        else:

            p = json.loads(json_string)

            return p
