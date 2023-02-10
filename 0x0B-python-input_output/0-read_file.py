#!/usr/bin/python3
"""function that reads a text file (UTF8) and prints it to stdout"""


def read_file(filename=""):
    """reading a file ``my_file.txt``"""

    with  open(filename, encoding="utf-8") as fileName:
        print(fileName.read(), end="")
