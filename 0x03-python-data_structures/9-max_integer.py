#!/usr/bin/python3
def max_integer(my_list=[]):
    if my_list:
        max = my_list[0]
        for i in my_list:
            if my_list[i] > max:
                return my_list[i]
    else:
        return None
