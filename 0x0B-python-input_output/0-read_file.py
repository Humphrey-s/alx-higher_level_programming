#!/usr/bin/python3
"""Defining read_file function."""


def read_file(filename=""):
    """Reads a file content in utf-8 encoding."""

    with open(filename, encoding="utf-8") as f:

        print(f.read(), end="")
