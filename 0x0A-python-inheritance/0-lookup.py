#!/usr/bin/python3
"""Defines a Function."""


def lookup(obj):
    """Returns a list of all attributes and methods in a class."""
    p = dir(obj)

    return list(p)
