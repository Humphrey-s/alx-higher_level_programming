#!/usr/bin/python3
hexa = "{num} = {x}"
for i in range (0, 99):
    print(hexa.format(num = i, x = hex(i)))
