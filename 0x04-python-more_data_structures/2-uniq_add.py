#!/usr/bin/python3

def uniq_add(my_list=[]):

    set_1 = set(my_list)

    list_1 = list(set_1)

    sum_1 = 0

    for i in range(len(list_1)):

        sum_1 += list_1[i]

    return sum_1
