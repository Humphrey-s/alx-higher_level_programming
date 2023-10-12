#!/usr/bin/python3
"""Defines a function."""


def pascal_triangle(n):
    """Returns a list of pascal triangle."""
    dl = []
    lld = []
    b = []

    if n <= 0:

        return dl

    if n == 0:
        return [1]

    for i in range(0, n):

        b.append([1])

        for a in range(0, i):

            if a == (i - 1) and i != 2:

                b[i].append(1)
                dl = b[i]
            elif i == 2:

                b[i].append(i)
                b[i].append(1)
                dl = b[i]

            else:

                if a + 1 < len(dl):

                    c = dl[a] + dl[a + 1]
                    b[i].append(c)

    if n > 1:

        b[2] = [1, 2, 1]

    return b
