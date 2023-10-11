#!/usr/bin/python3

"""Function that writes content of a file"""


def write_file(filename="", text=""):
    """
    Reads data from a file source

    Args:
        filename (str, optional): The file source.
    """

    with open(filename, 'w', encoding="utf-8") as f:
        return (f.write(text))
