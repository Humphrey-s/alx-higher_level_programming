#!/usr/bin/python3

def max_integer(my_list=[]):

    n = len(my_list)

    lis_t = my_list.copy

    max_n = []

    max_n = [-1024]

    if n == 0:

        return
    elif n == 1:

        return my_list[0]

    else:

        for i in range(n):

            if max_n[0] < my_list[i]:

                max_n[0] = my_list[i]

            elif max_n[0] >= my_list[i]:

                max_n[0] = max_n[0]

        return max_n[0]

