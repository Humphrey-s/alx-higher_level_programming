#!/usr/bin/python3

def print_matrix_integer(matrix=[[]]):

    n = len(matrix)
    ls = "{:d}"
    space = "{:s}"

    for i in range(n):

        lis_t = matrix[i]
        n1 = len(lis_t)

        for a in range(n1):

            print(ls.format(lis_t[a]), end='')

            if a != n1 - 1:

                print(space.format(" "), end='')

        print("")
