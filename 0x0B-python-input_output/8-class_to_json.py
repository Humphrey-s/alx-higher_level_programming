#!/usr/bin/python3
"""Defines class_to_json."""


def class_to_json(obj):
    """Converts instance of a class to json."""
    return obj.__dict__
