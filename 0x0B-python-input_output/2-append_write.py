#!/usr/bin/python3
"""Write a function that appends a string at the end of a text file (UTF8).
and returns the number of characters added
"""


def append_write(filename="", text=""):
    """append a string to the end of a file
    args:
        filename: the root of a file
        text: the text of the file to append at the end of the text file
    Retuens:
        The number of characters added to the file
    """
    with open(filename, 'a', encoding='utf-8') as f:
        return f.write(text)
