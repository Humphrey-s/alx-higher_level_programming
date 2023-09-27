#!/usr/bin/python3
"""Building a Class"""


class Square:
    """Defining a Class Square"""

    def __init__(self, size=0):
        """Initializing

        Args:
            size (int): size of square
        """

        if isinstance(size, int):

            if size < 0:
                raise ValueError("size must be >= 0")
            else:
                self.__size = size
        else:
            raise TypeError("size must be an integer")
