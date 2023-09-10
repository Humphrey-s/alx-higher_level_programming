#!/usr/bin/python3

def print_list_integer(my_list=[]):

    ls = my_list
    n = len(ls)

    ln = "{:d}"

    for i in range(0, n):

        print(ln.format(ls[i]))
