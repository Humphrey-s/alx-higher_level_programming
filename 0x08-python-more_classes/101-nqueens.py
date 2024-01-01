#!/usr/bin/python3
"""nqueens backtracking script"""
from sys import argv


if __name__ == "__main__":
    a = []
    if len(argv) != 2:
        print("Usage: nqueens N")
        exit(1)
    if argv[1].isdigit() is False:
        print("N must be a number")
        exit(1)
    m = int(argv[1])
    if m < 4:
        print("N must be at least 4")
        exit(1)

    # initialize the answer list
    for i in range(m):
        a.append([i, None])

    def _exists(y):
        """check that a queen does not already exist in that y value"""
        for x in range(m):
            if y == a[x][1]:
                return True
        return False

    def rej(x, y):
        """determines whether or not to reject the solution"""
        if (_exists(y)):
            return False
        i = 0
        while(i < x):
            if abs(a[i][1] - y) == abs(i - x):
                return False
            i += 1
        return True

    def clear(x):
        """clear function"""
        for i in range(x, m):
            a[i][1] = None

    def nqueens(x):
        """recursive backtrackung find the solution"""
        for y in range(m):
            clear(x)
            if rej(x, y):
                a[x][1] = y
                if (x == m - 1):
                    print(a)
                else:
                    nqueens(x + 1)
    nqueens(0)
