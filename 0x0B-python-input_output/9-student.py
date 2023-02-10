#!/usr/bin/python3
"""define a class that instance attributes"""


class Student:
    """Representation of class"""

    def __int__(self, first_name, last_name, age):
        """ Initialize a new Student.

        Args:
            first_name (str): The firstname of the student.
            last_name (str): The last name of the student.
            age (int): The age of the student.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

        def to_json(self):
            """ Get a dictionary representation of the student. """
            return self.__dic__
