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

            self._Square__size = size
