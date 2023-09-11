#!/usr/bin/python3

def print_matrix_integer(matrix=[[]]):

    n = len(matrix)

    for i in range(n):

        lis_t = matrix[i]
        
        n1 = len(lis_t)

        for a in range(n1):

            print("{:d}".format(lis_t[a]), end= '')

            if a != n:

                print(" ", end= '')

        print("")
