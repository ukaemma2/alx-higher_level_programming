#!/usr/bin/python3
""" function that writes a string to a text file (UTF8) and returns the number of characters written"""


def write_file(filename="", text=""):
    """write a string to a text and return the total character size

    Args:
        filename (str): The name of the file to write.
        text (str): The text to write to the file.
    Returns:
        The number of character written.
    """

    with open(filename, mode='w', encoding='utf-8') as f:
        return f.write(text)
