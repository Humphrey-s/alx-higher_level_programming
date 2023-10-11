#!/usr/bin/python3
"""Defines from_json_string."""
import json


def from_json_string(my_str):
    """Converts from Json to py."""
    return json.loads(my_str)
