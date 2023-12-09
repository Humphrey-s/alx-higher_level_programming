#!/usr/bin/python3
"""definition print_square fun"""


def print_square(size):

    try:

        if size is None:
            raise TypeError("size must be an integer")

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
            w = 0

            for h in range(0, size):

                while w < size:
                    square += "#"
                    w = w + 1
                w = 0
                if h + 1 != size:
                    square += "\n"
            print(square)
    except Exception as e:
        raise TypeError("size must be an integer")
