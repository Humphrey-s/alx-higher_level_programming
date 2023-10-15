#!/usr/bin/python3
"""Definition Rectangle."""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Rectangle Class."""

    def __init__(self, width, height):

        if self.integer_validator("width", width):

            self.__width = width

        if self.integer_validator("height", height):

            self.__height = height
