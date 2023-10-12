#!/usr/bin/python3
"""Defines a Class."""


class Student():
    """Student Class."""

    def __init__(self, first_name, last_name, age):

        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        
        p = self.__dict__
        d = {}

        if attrs == None:
            return p

        for i in range(0, len(attrs)):

            if isinstance(attrs, list) and isinstance(attrs[i], str):

                if attrs[i] == "first_name":
                    d["first_name"] = self.first_name

                if attrs[i] == "last_name":
                    
                    d["last_name"] = self.last_name

                if attrs[i] == "age":
                    d["age"] = self.age

        b = {k: v for k, v in sorted(d.items())}
        return b
