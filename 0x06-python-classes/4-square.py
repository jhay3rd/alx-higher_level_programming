#!/usr/bin/python3
"""class square which defines a Square"""


class Square:
    """Represents a square
    Attributes:
        __size (int): size of a square side
    """
    def __init__(self, size=0):
        """initializes the square
        Args:
            size (int): size of a square side
        Returns:
            None
        """
        self.size = size

    def area(self):
        """calculates the area of the square
        Returns:
            The calculated area of the square
        """
        return (self.__size) ** 2

    @property
    def size(self):
        """getter of __size
        Returns:
             Size of the square
        """
        return self.__size

    @size.setter
    def size(self, value):
        """setter of __size
        Args:
            value (int): the size of a side of the square
        Returns:
            None
        """
        if type(value) is not int:
            raise TypeError("size must be an integer")
        else:
            if value < 0:
                raise ValueError("size must be >= 0")
            else:
                self.__size = value
