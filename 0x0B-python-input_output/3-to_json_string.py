#!/usr/bin/python3
import json
"""Define to_json_string."""


def to_json_string(my_obj):
    """Converts obj to json rep of a string."""
    try:
        return json.dumps(my_obj)
    except:
        p = json.dumps(my_obj)

        return p
