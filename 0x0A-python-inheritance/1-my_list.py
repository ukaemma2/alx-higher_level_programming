#!/usr/bin/python3

"""A class that inherits from list"""


class MyList(list):
    """ mother class ``List Class``"""

    def print_sorted(self):
        """print the list in an ascending  sort"""
        print(sorted(self))
