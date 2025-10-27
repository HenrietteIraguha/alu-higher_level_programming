#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    new_matrix = []
    for row in matrix:
        results = [i ** i for i in row]
        new_matrix.append(results)
    return new_matrix
