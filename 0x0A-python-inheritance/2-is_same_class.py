#!/usr/bin/python3
"""Definition is_same_class function."""


def is_same_class(obj, a_class):

    if obj.__class__ == a_class:
        return True
    else:
        return False
