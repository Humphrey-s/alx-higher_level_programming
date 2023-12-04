#!/usr/bin/python3
"""Definition class Rectangle"""


class Rectangle:
    """Create rectangle shapes"""

    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):

        self.__width = width
        self.__height = height
        Rectangle.number_of_instances += 1

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, height):

        if isinstance(height, int):
            if height < 0:
                raise ValueError("height must be >= 0")

            self.__height = height
        else:
            raise TypeError("height must be an integer")

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, width):

        if isinstance(width, int):
            if width < 0:
                raise ValueError("width must be >= 0")

            self.__width = width
        else:
            raise TypeError("width must be an integer")

    def area(self):
        """Returns area of Rectagle"""
        return self.__width * self.__height

    def perimeter(self):
        """Returns perimeter of Rectangle"""
        if self.__width == 0 or self.__height == 0:
            return 0

        return 2 * (self.__width + self.__height)

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):

        try:
            area_1 = rect_1.area()
            area_2 = rect_2.area()

            if area_1 == area_2 or area_1 > area_2:
                return rect_1

            if area_2 > area_1:
                return area_2
        except Exception as e:
            if not isinstance(rect_1, Rectangle):
                raise TypeError("rect_1 must be an instance of Rectangle")
            if not isinstance(rect_2, Rectangle):
                raise TypeError("rect_2 must be an instance of Rectangle")

    def __str__(self):
        rec = ""
        for i in range(0, self.__height):
            for a in range(0, self.__width):
                if isinstance(self.print_symbol, str):
                    rec += self.print_symbol
                else:
                    rec += str(self.print_symbol)
            rec += "\n"
        return rec

    def __repr__(self):
        return f'Rectangle({self.__width}, {self.__height})'

    def __del__(self):
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")
