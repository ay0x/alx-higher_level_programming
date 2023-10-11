#!/usr/bin/python3

"""Function that writes an Object to a text file,
using a JSON representation
"""

import json


def save_to_json_file(my_obj, filename):
    """
    Writes an Object to a text file

    Args:
        my_obj (obj): The object.
        filename (str): The file name
    """

    with open(filename, 'w', encoding="utf-8") as f:
        json.dump(my_obj, f)
