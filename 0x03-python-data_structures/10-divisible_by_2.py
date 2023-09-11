#!/usr/bin/python3

def divisible_by_2(my_list=[]):
    new_list = []
    if my_list:
        for number in my_list:
            status = True if (number % 2 == 0) else False
            new_list.append(status)
        return new_list
    else:
        return []
