#!/usr/bin/python3

def add_tuple(tuple_a=(), tuple_b=()):

    n = len(tuple_a)
    n1 = len(tuple_b)

    new_tuple = ()

    if n < 2:

        for i in range(2):

            tuple_a += 0,

    if n1 < 2:

        for i in range(2):

            tuple_b += 0,

    new_tuple += tuple_a[0] + tuple_b[0],
    new_tuple += tuple_a[1] + tuple_b[1],

    return new_tuple
