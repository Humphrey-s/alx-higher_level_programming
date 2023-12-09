#!/usr/bin/python3


def add_integer(a, b=98):
    """adds a and b"""

    try:
        if isinstance(a, float) and isinstance(b, float):
            return int(a) + int(b)

        elif isinstance(a, float) and isinstance(b, int):
            return int(a) + b
        elif isinstance(a, int) and isinstance(b, float):
            return a + int(b)
        else:
            return a + b
    except Exception as e:

        if a is None:
            raise TypeError("a must be an integer")
        if b is None:
            raise TypeError("b must be an integer")

        if not isinstance(a, int) and not isinstance(a, float):
            raise TypeError("a must be an integer")

        if not isinstance(b, int) and not isinstance(b, float):
            raise TypeError("b must be an integer")
