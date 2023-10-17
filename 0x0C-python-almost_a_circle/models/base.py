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
