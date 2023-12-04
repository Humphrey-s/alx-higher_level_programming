#!/usr/bin/python3
"""Definition class Rectangle"""


class Rectangle:
    """Create rectangle shapes"""

    def __init__(self, width=0, height=0):

        if isinstance(width, int) and isinstance(height, int):
            if width < 0:
                raise ValueError("width must be >= 0")
            if height < 0:
                raise ValueError("height must be >= 0")

            self.__width = width
            self.__height = height
        else:
            if not isinstance(width, int):
                raise TypeError("width must be an integer")
            if not isinstance(height, int):
                raise TypeError("height must be an integer")

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

    def area(self):
        """Returns area of Rectagle"""
        return self.__width * self.__height

    def perimeter(self):
        """Returns perimeter of Rectangle"""
        if self.__width == 0 or self.__height == 0:
            return 0

        return 2 * (self.__width + self.__height)

    def __str__(self):
        rec = ""

        if self.__height <= 0 or self.__width <= 0:
            return rec

        for i in range(0, self.__height):

            for a in range(0, self.__width):
                rec += "#"

            if i + 1 != self.__height:
                rec += "\n"

        return rec
