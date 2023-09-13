#!/usr/bin/python3

def print_sorted_dictionary(a_dictionary):

    dict_s = sorted(a_dictionary)

    d = list(dict_s)

    for i in range(len(dict_s)):

        print("{}: {}".format(d[i], a_dictionary[d[i]]))
