#!/usr/bin/python3
"""Definition BaseGeometry."""


class BaseGeometry:
    """Class of area, per and etc."""

    def area(self):
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):

        if isinstance(value, int):

            if value > 0:
                pass
            else:
                raise ValueError("{} must be greater than 0".format(name))
        else:
            raise TypeError("{} must be an integer".format(name))
