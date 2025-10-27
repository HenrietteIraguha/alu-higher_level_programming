#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for row in matrix:
        # Format each integer in the row as string using str.format()
        formatted_nums = ["{:d}".format(num) for num in row]
        # Join them with space
        row_str = " ".join(formatted_nums)
        print(row_str)
