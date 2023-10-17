#!/usr/bin/python3
"""Square class"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """Geometrical square subclass."""

    def __init__(self, size, x=0, y=0, id=None):

        width = size
        height = size

        super().__init__(width, height, x, y, id)
