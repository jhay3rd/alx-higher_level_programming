#!/usr/bin/python3
"""Rectangle"""


class Rectangle:
    """"class attribute initialization"""
    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height

        def width(self):
            return self._width

        def width(self, value):
            if not isinstance(value. int):
                raise TypeError("width must be an integer")
            if value < 0:
                raise ValueError("width must be >= 0")

        def height(self):
            return self._height

        def height(self, value):
            if not isinstance(value, int):
                raise TypeError("height must be an integer")
            if value < 0:
                raise ValueError("height must be >= 0")

    def area(self):
        return self.width * self.height

    def perimeter(self):
        if self.width == 0 or self.height == 0:
            return 0
        else:
            return 2 * (self.width + self.height)
