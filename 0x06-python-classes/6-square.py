#!/usr/bin/python3
"""the class"""


class Square:
    """Definition"""

    def __init__(self, size=0, position=(0, 0)):
        self.size = size
        self.position = position

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

        p = self.__position

        if self.__size == 0:
            print("")
        else:
            for i in range(0, self.__size):

                for d in range(0, p[0]):

                    if (p[1] < 0) or not isinstance(p[1], int):
                        break
                    else:
                        print(" ", end='')

                for a in range(0, self.__size):

                    print("#", end='')
                    if a == self.__size - 1:
                        print("")

    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, position):

        if isinstance(position, tuple):

            if len(position) < 3:

                self.__position = position
            else:
                raise TypeError("position must be a tuple of 2 positive integers")
        else:
            raise TypeError("position must be a tuple of 2 positive integers")
