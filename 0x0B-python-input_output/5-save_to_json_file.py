#!/usr/bin/python3
"""save json object to a file"""
import json


def save_to_json_file(my_obj, filename):
    """save my_obj json to file"""

    with open(filename, "w", encoding="utf-8") as f:

        return f.write(json.dumps(my_obj))
