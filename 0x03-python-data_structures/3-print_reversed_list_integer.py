#!/usr/bin/python3

def print_reversed_list_integer(my_list=[]):

    lst = "{:d}"

    if my_list == None:

        print("".format(), end='')

    else:

        n = len(my_list)

        if n < 0 or n == 0:

            print("".format(), end='')

        else:

            for i in reversed(range(n)):

                print(lst.format(my_list[i]))
