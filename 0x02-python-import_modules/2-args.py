#!/usr/bin/python3

import sys

def main():

    n = len(sys.argv)
    a = n - 1

    if a == 0:

        print("{} argument.".format(a))
    else:
        print("{} arguments:".format(a))
        
        for i in range(1, n):

            print("{}: {}".format(i, sys.argv[i]))

if __name__ == "__main__":
    main()
