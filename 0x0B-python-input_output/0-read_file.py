#!/usr/bin/env python3
"""definition of function read_file"""


def read_file(filename=""):
    """reads and prints data in a file"""

    with open(filename, "r", encoding="utf-8") as f:

        read_data = f.read()
        print(read_data, end="")
