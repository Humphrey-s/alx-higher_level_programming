#!/usr/bin/python3
"""Define append_write."""


def append_write(filename="", text=""):
    """append or write to the end of file

    Args:
        filename (str): name of file to append
        text (str): txt to be appended
    Returns:
          nummber of characters appended
    """
    with open(filename, "a", encoding="utf-8") as f:

        return f.write(text)
