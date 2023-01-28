#!/usr/bin/python3
""" Square module definition
This module defines a simple `Square` class
"""


class Square:

    """A simple ``Square`` class
    Attribute:
        size (`int`): The size of the ``Square``.
    """

    def __init__(self, size=0):
        """Construct a ``Square`` Object.
        Args:
            size (`int`): The size of the ``Square``.
        Raises:
            TypeError: if ``size`` is not an integer
            ValueError: if ``size`` < 0
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:

            self.size = size

    def area(self):
        """compute the area of the ``Square``.
        Return:
            int: the area of ``Square``.
        """
        return self._Square__size**2

    @property
    def size(self):
        """
        Args:
            size (`int`): The size of the ``Square``.
        Raises:
            TypeError: if ``size`` is not an integer
            ValueError: if ``size`` < 0
        """
        return self._Square__size

    @size.setter
    def size(self, size):
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size mute be >= 0")
        else:
            self._Square__size = size

    def my_print(self):
        """
        prints in stdout the ``Square`` fill with #.
         Reurns:
            if ``size`` is equal to 0, print an empty line
        """
        if self.size:
            for i in range(self.size):
                for j in range(self.size):
                    print("#", end='')
                print()
        else:
            print()
