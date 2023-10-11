#!/usr/bin/python3

"""Function that append text of a file"""


def append_write(filename="", text=""):
    """
    Append data to a file source

    Args:
        filename (str, optional): The file source.
    """

    with open(filename, 'a', encoding="utf8") as f:
        return (f.write(text))
