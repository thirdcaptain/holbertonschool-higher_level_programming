#!/usr/bin/python3
"""
Defines a function that divides a matrix by a num
"""


def matrix_divided(matrix, div):
    """
    Divides a matrix by a constant
    """
    if not isinstance(div, float) and not isinstance(div, int):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    new_matrix = []
    """validate matrix"""
    if matrix is None:
        raise TypeError("matrix must be a matrix"
                        " (list of lists) of integers/floats")
    """validate matrix is made of lists"""
    length = len(matrix)
    for i in range(length):
        if not isinstance(matrix[i], list):
            raise TypeError("matrix must be a matrix"
                            " (list of lists) of integers/floats")
    """validate row lengths"""
    row_length = len(matrix[0])
    for i in range(length):
        if len(matrix[i]) != row_length:
            raise TypeError("Each row of the matrix must have the same size")
    """verify element types in matrix """
    for i in range(length):
        for element in matrix[i]:
            if not isinstance(element, float) and not isinstance(element, int):
                raise TypeError("matrix must be a matrix"
                                " (list of lists) of integers/floats")
    for i in range(length):
        new_matrix.append([])
        for element in matrix[i]:
            new_matrix[i].append(round((element / div), 2))
    return new_matrix
