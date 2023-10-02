#!/usr/bin/python3
"""Creating a class."""


class Rectangle:
    """Defining Rectangle Class."""

    def __init__(self, width=0, height=0):
        """initializing instance attributes."""

        self.width = width
        self.height = height

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, width):

        if isinstance(width, int):

            if width < 0:

                raise ValueError("width must be >= 0")
            else:
                self.__width = width
        else:
            raise TypeError("width must be an integer")

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, height):

        if isinstance(height, int):

            if height < 0:

                raise ValueError("height must be >= 0")
            else:
                self.__height = height
        else:
            raise TypeError("height must be an integer")

    def area(self):

        return self.__height * self.__width

    def perimeter(self):

        return 2 * (self.__height + self.__width)
