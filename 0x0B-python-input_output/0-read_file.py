#!/usr/bin/pthon3

def read_file(filename=""):

    with open(str(filename), encoding="utf-8") as f:

        for line in f:

            print(line, end="")
