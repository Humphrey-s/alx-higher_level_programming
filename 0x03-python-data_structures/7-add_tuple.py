#!/usr/bin/python3

def add_tuple(tuple_a=(), tuple_b=()):


    n = len(tuple_a)
    n1 = len(tuple_b)

    n_tuple = ()

    if n > n1:

        for i in range(n - n1):

            tuple_b += 0,

        for a in range(len(tuple_a)):

            n_tuple += tuple_a[a] + tuple_b[a],

        return n_tuple

    elif n < n1:
        
        for i in range(n1 - n):

            tuple_a += 0,

        for a in range(len(tuple_a)):

            new_tuple += tuple_a[a] + tuple_b[a],

        return n_tuple
    else:

        for i in range(len(tuple_a)):

            n_tuple += tuple_a[i] + tuple_b[i],

        return n_tuple
