#!/usr/bin/python3
"""the class"""


class Square:
    """Definition"""

    def __init__(self, size=0):
        self.size = size

    @property
    def size(size):
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

        a = self.size ** 2
        return a

    def my_print(self):

        if self.__size == 0:
            print("")
        else:
            for i in range(0, self.__size):

                for a in range(0, self.__size):

                    print("#", end='')
                    if a == self.__size - 1:
                        print("")
