#!/usr/bin/python3

import sys

def main(): 
    n = len(sys.argv)
    a = n - 1

    if a == 0:
        print("{} arguments.".format(a))
    else:
        if a == 1:
            print("1 argument:".format())
        else:
            print("{} arguments:".format(a))

    for i in range(1, n):
        print("{}: {}".format(i, sys.argv[i]))

if __name__ == "__main__":
    main()
