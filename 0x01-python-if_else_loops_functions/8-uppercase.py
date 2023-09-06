#!/usr/bin/python3


def uppercase(str):


    n = len(str)
    i = 0

    while i < n:

        c = ord(str[i])

        if c > 96 and c < 124:

            c = ord(str[i]) - 32

        char = chr(c)
        print("{}".format(char), end= '')

        i = i + 1

    print(f"")
