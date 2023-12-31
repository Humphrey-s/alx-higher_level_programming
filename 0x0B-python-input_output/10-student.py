#!/usr/bin/python3
"""Definition Student Class"""


class Student:
    """Class Student"""

    def __init__(self, first_name, last_name, age):
        """initialization"""

        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """returns Json representation of an instance of Student"""

        if isinstance(attrs, list):

            dic_t = {}

            for a in attrs:

                try:
                    dic_t[a] = getattr(self, a)
                except AttributeError:
                    pass

            return dict(sorted(dic_t.items()))

        else:
            dic_t = self.__dict__

            return dict(sorted(dic_t.items()))
