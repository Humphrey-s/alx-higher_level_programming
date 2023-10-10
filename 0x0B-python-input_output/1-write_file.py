#!/usr/bin/python3
"""Defines write file function."""


def write_file(filename="", text=""):
    """Writes to a file."""

    with open(filename, "w", encoding="utf-8") as f:

        return f.write(text)
