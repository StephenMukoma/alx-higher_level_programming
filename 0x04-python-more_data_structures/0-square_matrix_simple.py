#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    square = []
    for i in matrix:
        s = list(map(lambda x : x ** 2, i))
        square.append(s)
    return square
