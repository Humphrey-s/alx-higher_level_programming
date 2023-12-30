#!/usr/bin/python3
"""definition class_to_json"""
import json


def class_to_json(obj):
    """convert class to json"""

    return json.dumps(obj.__dict__)
