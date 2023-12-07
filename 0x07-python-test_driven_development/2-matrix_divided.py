#!/usr/bin/python3
"""definition of matrix_divided"""


def llcopy(matrix):
    """copy matrix"""
    if not isinstance(matrix, list):
        return matrix

    dest = matrix[:]

    for i in range(0, len(matrix)):
        row = matrix[i]

        if not isinstance(row, int):
            dest[i] = row[:]

    return dest


def matrix_divided(cmatrix, div):
    """divides all elements in a matrix"""

    matrix = llcopy(cmatrix)

    if div == 0:
        raise ZeroDivisionError("division by zero")

    if not isinstance(matrix, list) or len(matrix) == 0 or matrix is None:
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")

    next_l = matrix[0]
    c = 0

    for a in range(0, len(matrix)):

        index_l = matrix[a]

        if isinstance(index_l, int) or isinstance(index_l, float):
            c = -1
            break

        if not isinstance(index_l, list):
            raise TypeError("matrix must be a matrix (list of lists) of integers/floats")

        if len(next_l) != len(index_l):
            raise TypeError("Each row of the matrix must have the same size")

    if c == -1:

        for d in range(0, len(matrix)):

            element = matrix[d]
            if isinstance(element, int) or isinstance(element, float):
                if isinstance(div, int) or isinstance(div, float):
                    matrix[d] = round(element / div, 2)
                else:
                    raise TypeError("div must be a number")
        return (matrix)

    for e in range(0, len(matrix)):

        row = matrix[e]
        for i in range(0, len(row)):
            element = row[i]

            if isinstance(element, int):

                if isinstance(div, int) or isinstance(div, float):
                    row[i] = round(element / div, 2)
                else:

                    raise TypeError("div must be a number")

            elif isinstance(element, float):

                if isinstance(div, int) or isinstance(div, float):
                    row[i] = round(element / div, 2)
                else:
                    raise TypeError("div must be a number")
            else:
                raise TypeError("matrix must be a matrix (list of lists) of integers/floats")

    return matrix
