#!/usr/bin/python3
"""Definition of inherits_from."""


def inherits_from(obj, a_class):
    """Checks for inheritance."""

    a = type(obj)

    if a_class is not bool:

        if isinstance(obj, a_class) or issubclass(a, a_class):
            return True
        else:
            return False
    else:

        return False
