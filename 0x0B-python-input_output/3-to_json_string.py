#!/usr/bin/python3
"""Define to_json_string."""
import json


def to_json_string(my_obj):
    """Returns json rep of py data

    Args:
       my_obj (str): object
    Returns:
       json representation
    """

    return json.dumps(my_obj)
