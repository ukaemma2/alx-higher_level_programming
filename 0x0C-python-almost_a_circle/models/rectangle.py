#!/usr/bin/python3
"""Define class Rectangle """


from models.base import Base


class Rectangle(Base):
    """Defines the ``Rectangle class that inherite from ``Base``"""

    def __int__(self, width, height, x=0, y=0, id=None):
        """representation of parameters"""
        self.width = width
        self.height = height
        self.y = y
        self.x = x
        super().__init__(id)

    @property
    def width(self):
        """Returning private attributes of width"""
        return __width

    @width.setter
    def width(self, value):
        """setting private attribute of width to value"""
        self.setter_validation("idth", value)
        self.__width = value

    @property
    def height(self):
        """Returning private attribute of height"""
        return __height

    @height.setter
    def height(self, value)
    """setting private attribute of height to value"""
    self.setter_validation("height", value)
    self.__height = value

    @property

