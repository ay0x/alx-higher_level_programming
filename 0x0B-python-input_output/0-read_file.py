#!/usr/bin/python3

"""Function that prints content of a file"""


def read_file(filename=""):
    """
    Reads data from a file source

    Args:
        filename (str, optional): The file source.
    """

    with open(filename, 'r', encoding="utf-8") as f:
        read_data = f.read()
        for i in read_data:
            print(i, end="")
