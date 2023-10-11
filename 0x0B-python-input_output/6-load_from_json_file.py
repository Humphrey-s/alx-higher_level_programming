#!/usr/bin/python3
"""Define load_from_json_file."""
import json


def load_from_json_file(filename):
    """loads from json in file to py."""
    with open(filename) as f:
        return json.load(f)
