#!/usr/bin/python3

def print_matrix_integer(matrix=[[]]):
    for row in matrix:
        for cols in row:
            print('{:d}'.format(cols), end=' ')
        print()
