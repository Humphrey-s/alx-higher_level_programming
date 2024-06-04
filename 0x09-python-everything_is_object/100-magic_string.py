#!/usr/bin/python3
def magic_string():
    magic_string.s = "BestSchool" if not hasattr(magic_string, "s") else magic_string.s + ", BestSchool"
    return magic_string.s
