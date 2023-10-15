#!/usr/bin/python3
"""Definition Rectangle."""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Rectangle Class."""

    def __init__(self, width, height):

        super().integer_validator("width", width)
        self.__width = width

        super().integer_validator("height", height)
        self.__height = height

    def area(self):

        return self.__width * self.__height

    def __str__(self):

        string = "[" + str(self.__class__.__name__) + "] "
        string += str(self.__width)
        string += ("/" + str(self.__height))

        return string
