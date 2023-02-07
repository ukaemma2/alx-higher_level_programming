#!/usr/bin/python3
"""Defines a base geometry class BaseGeometry."""


class BaseGeometry:
    """Represent base geometry."""

    def area(self):
        """Not implemented."""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validate the names and value of the object
        args:
            Value: is != int
            Value: is <= 0
        Raises:
            TypeError: <name> must be an integer
            ValueError: <name> must be greater than 0
        """
        self.name = name
        self.value = value

        if type(value) != int:
            raise TypeError('{} must be an integer'.format(name))
        if value <= 0:
            raise ValueError('{} must be greater than 0'.format(name))
