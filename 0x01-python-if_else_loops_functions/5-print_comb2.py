#!/usr/bin/python3

num = "{l1}"
num2 = "{b}, "
for n in range(0, 100):
    if n < 10:
        print(num.format(l1 = 0), end= '')

    print(num2.format(b = n), end= '')
