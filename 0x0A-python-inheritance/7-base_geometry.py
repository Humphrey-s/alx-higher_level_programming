#!/usr/bin/python3
"""Definition BaseGeometry."""


class BaseGeometry:
    """Class of area, per and etc."""

    def area(self):
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):

        if type(value) != int:

            raise TypeError("{} must be an integer".fomat(name))
        if value <= 0:

            raise ValueError("{} must be greater than 0".format(name))
