#!/usr/bin/python3

"""
Module sorts lists
"""


class MyList(list):

    """MyList is a child class of superclass list """

    def print_sorted(self):
        """Function sorts lists"""
        sorted_list = sorted(self)
        print(sorted_list)
