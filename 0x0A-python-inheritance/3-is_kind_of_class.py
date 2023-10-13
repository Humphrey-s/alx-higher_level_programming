#!/usr/bin/python3
"""Definition is_kind_of_class."""


def is_kind_of_class(obj, a_class):
    """Returns true if object is an instance or is a subclass of."""

    if isinstance(obj, a_class):
        return True
    else:
        return False
