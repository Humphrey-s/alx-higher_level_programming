#!/usr/bin/python3
"""LockedClass"""


class LockedClass():
    """allows class only one attribute"""
    __slots__ = ('first_name')

    def __init__(self):
        self.first_name = 'first_name'
