#!/usr/bin/python3
"""definition Student"""


class Student:

    def __init__(self, first_name, last_name, age):
        """initialize student"""

        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """return class json representation"""

        return self.__dict__
