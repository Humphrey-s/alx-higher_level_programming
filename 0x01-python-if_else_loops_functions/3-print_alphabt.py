#!/usr/bin/python3

txt = "{character}"
for i in range(97, 123):
    if i == 101 and True or i == 113 and True:
        continue
    else:
        print(txt.format(character = chr(i)), end='')
