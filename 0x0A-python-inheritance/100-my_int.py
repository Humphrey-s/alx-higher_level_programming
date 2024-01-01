#!/usr/bin/python3
"""class MyInt"""


class MyInt(int):
    """class MyInt that inherits from int"""

    def __new__(cls, *args, **kwargs):
        """new instance of the class"""
        return super(MyInt, cls).__new__(cls, *args, **kwargs)

    def __eq__(self, other):
        """function"""
        return int(self) != other

    def __ne__(self, other):
        """method"""
        return int(self) == other
