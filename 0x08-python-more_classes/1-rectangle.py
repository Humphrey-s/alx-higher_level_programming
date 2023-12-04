#!/usr/bin/python3
"""Definition class Rectangle"""


class Rectangle:
    """Create rectangle shapes"""

    def __init__(self, width=0, height=0):

        self.__width = width
        self.__height = height

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, height):

        if isinstance(height, int):
            if height < 0:
                raise ValueError("height must be >= 0")

            self.__height = height
        else:
            raise TypeError("height must be an integer")

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, width):

        if isinstance(width, int):
            if width < 0:
                raise ValueError("width must be >= 0")

            self.__width = width
        else:
            raise TypeError("width must be an integer")
