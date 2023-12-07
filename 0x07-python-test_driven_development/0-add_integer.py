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
        raise TypeError(" a must be an integer or b must be an integer")
