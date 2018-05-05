#!/usr/bin/python3
"""Defines a function that divides a matrix by a num"""

def matrix_divided(matrix, div):
    """Divides a matrix by a constant"""
    new_matrix = []
    length = len(matrix)

    for i in range(length):
        new_matrix.append([])
        for element in matrix[i]:
            new_matrix[i].append(round((element / div), 2))

    return new_matrix
