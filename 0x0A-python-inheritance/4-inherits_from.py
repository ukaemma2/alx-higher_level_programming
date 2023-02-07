#!/usr/bin/python3
"""function that returns True or False"""


def inherits_from(obj, a_class):
    """checking if the object is an instances of a class that that inherited
    directly or indirectly.

    args:
        obj (any): The object to check.
        a_class (type): The class to match the type of obj.
    Returns:
        if obj is an instance of inherited class directly or indirectly - True
        Otherwise - False.
    """
    if issubclass(type(obj), a_class) and type(obj) != a_class:
        return True
    return False
