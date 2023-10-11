#!/usr/bin/python3
"""Defines class_to_json."""
import json


def class_to_json(obj):
    """Converts instance of a class to json."""
    f = json.dumps(obj.__dict__)
    p = json.loads(f)
    return p
