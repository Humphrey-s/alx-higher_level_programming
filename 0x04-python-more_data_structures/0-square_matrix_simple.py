#!/usr/bin/python3

def square_matrix_simple(matrix=[]):

    n = len(matrix)

    new_matrix = []

    new_matrix = list(matrix)


    for i in range(n):

        new_matrix[i] = list(map(lambda x: x ** 2, matrix[i]))


    return new_matrix
