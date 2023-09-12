#!/usr/bin/python3

def print_reversed_list_integer(my_list=[]):

    lst = "{:d}"
    n = len(my_list)

    if n < 0 or n == 0:

        print("".format(), end= '')

    for i in reversed(range(n)):

        print(lst.format(my_list[i]))
