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
        """getter size"""

        return self.width

    @size.setter
    def size(self, size):
        """setter size"""

        self.width = size
        self.height = size

    def update(self, *args, **kwargs):
        """update arguments"""

        if args is not None:

            for i in range(0, len(args)):

                if i == 0:

                    self.id = args[i]
                if i == 1:

                    self.size = args[i]

                if i == 2:

                    self.x = args[i]
                if i == 3:
                    self.y = args[i]

        for key in kwargs:

            if key == "id":

                self.id = kwargs[key]
            if key == "size":

                self.size = kwargs[key]
            if key == "x":

                self.x = kwargs[key]
            if key == "y":

                self.y = kwargs[key]
