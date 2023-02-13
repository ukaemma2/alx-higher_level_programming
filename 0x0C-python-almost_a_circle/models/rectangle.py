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
        return self.__width

    @width.setter
    def width(self, value):
        """setting private attribute of width to value"""
        self.setter_validation("width", value)
        self.__width = value

    @property
    def height(self):
        """Returning private attribute of height"""
        return self.__height

    @height.setter
    def height(self, value):
        """setting private attribute of height to value"""
        self.setter_validation("height", value)
        self.__height = value

    @property
    def x(self):
        """Returning private attribute of x """
        return self.__x

    @x.setter
    def x(self, value):
        """setting private attribute of x to value"""
        self.setter_validation("x", value)
        self.__x = value

    @property
    def y(self):
        """Returning private attribute of y"""
        return self.__y

    @y.setter
    def y(self, value):
        """setting private attribute of y to value"""
        self.setter_validation("y", value)
        self.__y = value


    @staticmethod
    def setter_validation(attribute, value):
        if (value) is not int:
            raise TypeError('{} must be an integer'.format(attribute))
        if attribute == 'x' or attribute == 'y':
            if value < 0:
                raise ValueError('{} must be >= 0'.format(attribute))
        elif value <= 0:
            raise ValueError('{} must be >= 0'.format(attribute))

    def __str__(self):
        """overwritten the str method"""
        return '[Rectangle] ({} {}/{} - {}/{}'.format(self.id, self.x, self.y,
                                                    self.width, self.height)
