#!/usr/bin/python3
""""Rectangle Modules class"""


class Rectangle:

    """Define a ``Rectangle`` class"""


    def __int__(self, width=0, height=0):
        """Create a ``Rectangle`` instance.
        Args:
            Width: define the width of the ``Rectangle``
            height: defines the height of the ``Rectangle``
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """property of width that define the lenght of ``Rectangle``
        Raises:
            TypeError: if the width != int
            ValueError: if width < 0
        """
        return self.__width

    @width.setter
    def width(self, value):
        """Sets the width of a Rectangle instance
        Args:
            value: value of the width, must be a positive integer
        """
        if not isinstance(value, int):
            raise TypeError('width must be an integer')
        if value < 0:
            raise ValueError('width must be >= 0')
        self.__width = value

    @property
    def height(self):
        """Property of height that define the lenght of ``Rectangle``
        Raises:
            TypeError: if the height != int
            ValueError: if height < 0
        """
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError('height must be an integer')
        if value < 0:
            raise ValueError('height must be >= 0')
        self.__height = value

