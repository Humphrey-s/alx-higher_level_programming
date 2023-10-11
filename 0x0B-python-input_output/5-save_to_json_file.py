#!/usr/bin/python3
"""Defines save_to_json_file."""
import json


def save_to_json_file(my_obj, filename):
    """save json rep of py to a file"""
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(my_obj, f)
