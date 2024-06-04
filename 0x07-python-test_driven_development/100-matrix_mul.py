#!/usr/bin/python3
"""module for matrix multiplication"""


def check_list_type(lst):
    """identifies if a list has any other type"""
    for i in lst:
        if isinstance(i, list):
            for a in i:
                if not isinstance(a, int):
                    return 0
        else:
            if not isinstance(a, int):
                return 0

    else:
        return 1


def check_list_shape(lst):
    """checks if a lst is a rectangle"""
    lst_lengths = []

    lst_lengths = [len(i) for i in lst if isinstance(i, list)]

    b = lst_lengths[0]

    for a in lst_lengths:
        if a != b:
            return 0
    else:
        return 1


def get_columns(matrix):
    """get columns from a matrix"""
    columns = []
    Ncolumns = len(matrix[0])

    for i in range(0, Ncolumns):
        lst = [row[i] for row in matrix]
        columns.append(lst)

    return columns


def matrix_mul(m_a, m_b):
    """multiplies 2 matrix"""

    if not isinstance(m_a, list):
        raise TypeError("m_a must be a list")
    if not isinstance(m_b, list):
        raise TypeError("m_b must be a list")
    if not m_a:
        raise ValueError("m_a can't be empty")
    if not m_b:
        raise ValueError("m_b can't be empty")
    if check_list_type(m_a) == 0:
        raise TypeError("m_a should contain only integers or floats")
    if check_list_type(m_b) == 0:
        raise TypeError("m_b should contain only integers or floats")
    if check_list_shape(m_a) == 0:
        raise TypeError("each row of m_a must be of the same size")
    if check_list_shape(m_b) == 0:
        raise TypeError("each row of m_b must be of the same size")
    if len(m_a[0]) != len(m_b):
        raise ValueError("m_a and m_b can't be multiplied")

    columns = get_columns(m_b)
    product = []

    for row in m_a:
        lst = []
        for column in columns:
            a = 0
            ij = 0
            for i in row:
                j = column[a]
                ij += i * j
                a += 1
            else:
                lst.append(ij)
        else:
            product.append(lst)
    else:
        return product
