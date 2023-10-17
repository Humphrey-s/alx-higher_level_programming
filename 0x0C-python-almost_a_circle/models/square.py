#!/usr/bin/python3
"""Square class"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """Geometrical square subclass."""

    def __init__(self, size, x=0, y=0, id=None):
        """initialization"""

        super().__init__(size, size, x, y, id)

    @property
    def size(self):

        return self.width

    @size.setter
    def size(self, size):

        self.width = size
        self.height = size
