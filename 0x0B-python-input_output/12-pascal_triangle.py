#!/usr/bin/python3
"""function pascal_triangle"""


def pascal_triangle(n):
    """returns pascal_triangle upto n"""

    if (n <= 0):
        return []

    if (n == 1):
        return [[1]]

    pascal = [[1], [1, 1], [1, 2, 1]]

    ls_t = []
    prev_lst = []

    for i in range(4, n + 1):

        prev_lst = pascal[i - 2]
        ls_t.append(1)

        for b in range(0, len(prev_lst)):

            for a in range(1, len(prev_lst)):

                if a - 1 == b:
                    ls_t.append(prev_lst[b] + prev_lst[b + 1])
                    break

        ls_t.append(1)
        pascal.append(ls_t)
        b = 0
        a = 0
        ls_t = []
        prev_lst = []

    return pascal
