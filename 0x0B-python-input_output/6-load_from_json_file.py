#!/usr/bin/python3
"""definition load_from_json_file"""
import json


def load_from_json_file(filename):
    """convert json in a file to string"""

    with open(filename, "r", encoding="utf-8") as f:

        encoded = f.read()

        return json.loads(encoded)
