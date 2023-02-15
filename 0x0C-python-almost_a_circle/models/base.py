#!/usr/bin/python3
"""Defines a base model class."""


import json


class Base:
    """Represent the base model.
    Represents the "base" for all other classes in project 0x0C*.
    Attributes:
        __nb_objects (int): The number of instantiated Bases.
    """

    __nb_objects = 0

    def __init__(self, id=None):
        """Initialize a new Base.
        Args:
            id (int): The identity of the new Base.
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        '''JSON represensation for sharing data
        Return the JSON serialization of a list of dicts.
        Args:
            list_dictionaries (list): A list of dictionaries
        '''

        if list_dictionaries is None or list_dictionaries == '[]':
            return "[]"
        else:
            return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        '''updating class Base' that represent object
        args:
            list_objts: l of object
        '''
        filename = cls.__name__ + ".json"
        with open(filename, 'w') as jsonfile:
            if list_objs is None:
                jsonfile.write("[]")
            else:
                list_dicts = [o.to_dictionary() for o in list_objs]
                jsonfile.write(Base.to_json_string(list_dicts))

    @staticmethod
    def from_json_string(json_string):
        '''updating the class Base from json to string
        Args:
            json_string (list): list of dictionaries
        '''

        if json_string is None or json_string == '[]':
            return []
        else:
            return json.loads(json_string)
