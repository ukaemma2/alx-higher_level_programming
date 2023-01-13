#!/usr/bin/python3

def print_matrix_integer(matrix=[[]]):
    if len(matrix[0]) != 0:
        rows = len(matrix)
        cols = len(matrix[0])
        for row in range(rows):
            for col in range(cols):
                if col == cols - 1:
                    print('{:d}'.format(matrix[row][col]))
                else:
                    print('{:d}'.format(matrix[row][col]), end=' ')
    else:
        print()
