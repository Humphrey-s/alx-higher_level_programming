#!/usr/bin/python3
"""Representation of a Class."""


class Square:
    """Defining Square."""

    def __init__(self, size=0):
        """initializing Square

        Args:
            size (int): size of square.
        """
        if isinstance(size, int):

            if size < 0:

                raise ValueError("size must be >= 0")
            else:

                self.__size = size

        else:
            raise TypeError("size must be an integer")

    def area(self):

        a = self.__size

        return a * a
