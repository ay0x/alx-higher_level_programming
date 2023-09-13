#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    new_list = []
    for row in matrix:
        new_row = []
        for element in row:
            new_row.append(element * element)
        new_list.append(new_row)
    return new_list
