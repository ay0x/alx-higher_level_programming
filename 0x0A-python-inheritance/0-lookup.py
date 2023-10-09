#!/usr/bin/python3

"""
Module that returns the list of
available attributes and methods of an object
"""


def lookup(obj):
    """Returns the list of attributes of an object

    Args:
        obj (class): Class or object

    Returns:
        list: Objects or class
    """
    return (dir(obj))
