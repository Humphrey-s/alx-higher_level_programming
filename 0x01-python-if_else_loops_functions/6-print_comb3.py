#!/usr/bin/python3
b = 0
num = 89
for n in range(0, 10):

    for i in range(b, 10):

        if i == n and True:
            continue
        else:

            if n == 8 and i == 9 and True:
                print("{}".format(num))
            else:
                print("{}".format(n), end= '')
                print("{}".format(i), end= ', ')

    b = n + 1
