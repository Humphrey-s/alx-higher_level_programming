#!/usr/bin/python3

import sys

def main():
    
    n = len(sys.argv)

    a = n - 1
    sum1 = 0

    for i in range(1, n):

        sum1 += int(sys.argv[i])

    print("{}".format(sum1))

if __name__ == "__main__":
    main()
