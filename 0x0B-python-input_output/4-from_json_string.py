#!/usr/bin/python3

"""
Function that returns an object (Python data structure)
represented by a JSON string
"""

import json


def from_json_string(my_str):
    """Returns the JSON representation of an object

    Args:
        my_str (_type_): The String

    Returns:
        str: The object (Python data structure) 
    """

    return (json.loads(my_str))
