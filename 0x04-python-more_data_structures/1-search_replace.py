#!/usr/bin/python3

def search_replace(my_list, search, replace):

    new_list = []

    new_list = my_list[:]

    n = len(my_list)

    new_list = list(map(lambda x: x == search, my_list))

    for i in range(n):

        if new_list[i] is True:

            new_list[i] = replace
        else:
            new_list[i] = my_list[i]

    return new_list
