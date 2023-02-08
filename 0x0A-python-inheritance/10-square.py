#!/usr/bin/python3
"""A class Square that inherits from Rectangle (9-rectangle.py)"""

Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """initializ size and validate the integer"""

    def __int__(self, size):
        """validate the size of the integer
        args:
            size (int) size of the Rectangle
        """
        self.integer_validate("size", size)
        super().__int__(size, size)
        self.__size = size
