#!/usr/bin/python3
"""Definition  Rectangle subclass."""
from models.base import Base


class Rectangle(Base):
    """Subclass Rectangle"""

    def __init__(self, width, height, x=0, y=0, id=None):

        super().__init__(id)

        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, width):

        n = width
        if isinstance(n, int):

            if n <= 0:

                raise ValueError("width must be > 0")
            else:
                self.__width = width
        else:
            raise TypeError("width must be an integer")

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, height):

        n = height

        if isinstance(n, int):

            if n <= 0:

                raise ValueError("height must be > 0")
            else:
                self.__height = height

        else:
            raise TypeError("height must be an integer")

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, x):

        if isinstance(x, int):

            if x < 0:

                raise ValueError("x must be >= 0")
            else:
                self.__x = x

        else:
            raise TypeError("x must be an integer")

    @property
    def y(self):
        return self.__x

    @y.setter
    def y(self, y):

        if isinstance(y, int):

            if y < 0:

                raise ValueError("y must be >= 0")
            else:
                self.__y = y

        else:
            raise TypeError("y must be an integer")

    def area(self):

        return self.__height * self.__width

    def display(self):

        a = self.__height
        b = self.__width
        x = self.__x
        y = self.__y

        for yc in range(0, y):

            print("")

        for h in range(0, a):

            for xc in range(0, x):

                print(" ", end="")

            for w in range(0, b):

                print("#", end="")
            print("")

    def __str__(self):

        string = "[" + str(self.__class__.__name__) + "] ("
        string += str(self.id) + ") " + str(self.__x) + "/" + str(self.__y)
        string += " - " + str(self.__width) + "/" + str(self.__height)

        return string
