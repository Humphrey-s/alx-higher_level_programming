#!/usr/bin/python3
"""Defines the class Mylist."""


class MyList(list):
    """Sub class of list that sorts."""

    def print_sorted(self):

        self.sort()
