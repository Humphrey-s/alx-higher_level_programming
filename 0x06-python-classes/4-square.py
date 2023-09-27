#!/usr/bin/python3
"""Set/ build class."""


class Square:
    """Definition."""

    def __init__(self, size=0):

        self.size = size

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, size):

        if isinstance(size, int):

            if size < 0:
                raise ValueError("size must be >= 0")
            else:
                self.__size = size
        else:
            raise TypeError("size must be an integer")

    def area(self):
        """returns area of square"""

        a = self.__size
        return a * a
