#!/usr/bin/python3


def uppercase(str):

    n = len(str)
    i = 0

    while i < n:

        c = ord(str[i])

        if c > 96 and c < 124:

            l = c - 97

            print(f"{chr(65 + l)}", end= '')

        else:
            print(f"{str[i]}", end= '')


        i = i + 1

    print(f"")
