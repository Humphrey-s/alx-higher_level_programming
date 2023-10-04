#!/usr/bin/python3
"""Creating a class."""


class Rectangle:
    """Defining Rectangle Class."""

    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """initializing instance attributes."""

        self.width = width
        self.height = height
        string = None

        self.print_symbol = self.print_symbol
        Rectangle.number_of_instances += 1

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

        if self.__width == 0 or self.__height == 0:

            return 0

        return self.__height * self.__width

    def perimeter(self):

        if self.__width == 0 or self.__height == 0:

            return 0

        return 2 * (self.__height + self.__width)

    def __str__(self):

        h = self.__height
        w = self.__width

        if isinstance(self.print_symbol, list):

            string = []

            for i in range(0, h):

                for i in range(0, w):

                    string.append(self.print_symbol)

            return str(string)

        string = ""

        for i in range(0, h):

            for a in range(0, w):

                string += self.print_symbol

            if i + 1 != h:

                string += "\n"

        if h == 0 or w == 0:

            return ""

        self.string = string

        return self.string

    def __repr__(self):

        b = "Rectangle" + "(" + str(self.width) + ", " + str(self.height) + ")"

        return b

    def __del__(self):

        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")
