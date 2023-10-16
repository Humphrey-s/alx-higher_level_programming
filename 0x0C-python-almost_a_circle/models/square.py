#!/usr/bin/python3
"""Class Square."""
from models.rectangle import Rectangle


class Square(Rectangle):
    """Definition Square subclass."""

    def __init__(self, size, x=0, y=0, id=None):

        super().__init__(size, size, x, y, id)
