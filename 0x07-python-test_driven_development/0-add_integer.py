#!/usr/bin/python3
"""definition function add_integer"""


def add_integer(a, b=98):
    """adds a and b"""

    try:
        if a != a:
            a = 89
        if b != b:
            b = 89

        if isinstance(a, float) and isinstance(b, float):
            return int(a) + int(b)

        elif isinstance(a, float) and isinstance(b, int):
            return int(a) + b
        elif isinstance(a, int) and isinstance(b, float):
            return a + int(b)
        else:
            return a + b

    except Exception as e:

        if a is None or (type(a) is not int and type(a) is not float):
            raise TypeError("a must be an integer")
        if b is None or (type(b) is not int and type(b) is not float):
            raise TypeError("b must be an integer")
