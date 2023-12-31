#!/usr/bin/python3
"""definition append_after"""


def append_after(filename="", search_string="", new_string=""):
    """inserts line to a file, after line containing a specific string"""

    string = ""

    with open(filename, "r+", encoding="utf-8") as f:

        for line in f:

            string += line

            if search_string in line:
                string += new_string

        f.seek(0)
        f.write(string)
