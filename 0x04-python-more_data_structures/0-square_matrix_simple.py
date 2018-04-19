#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    new_matrix = []
    for i in range(len(matrix)):
        new_matrix.append([])
        for element in matrix[i]:
            new_matrix[i].append(element ** 2)
    return new_matrix
