#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for row in range(len(matrix)):
        for item in range(len(matrix[row])):
            print("{:d}".format(matrix[row][item]), end="")
            if item != len(matrix[row]) - 1:
                print(" ", end="")
        print("")
