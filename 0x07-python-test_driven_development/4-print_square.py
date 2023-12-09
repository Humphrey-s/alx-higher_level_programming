#!/usr/bin/python3
"""definition print_square fun"""


def print_square(size):

    if isinstance(size, float) and size < 0:
        raise TypeError("size must be an integer")

    if not isinstance(size, int):
        raise TypeError("size must be an integer")

    if size < 0:
        raise ValueError("size must be >= 0")

    if size == 0:
        pass

    else:
        square = ""

        for h in range(0, size):

            for l in range(0, size):
                square += "#"

            if h + 1 != size:
                square += "\n"

        print(square)
