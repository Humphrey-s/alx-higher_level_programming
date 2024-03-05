#!/usr/bin/python3
"""prints the error code incase any"""
import requests
import sys

if __name__ == "__main__":

    r = requests.get(sys.argv[1])
    s_code = r.status_code

    if s_code > 399:
        print("Error code: {}".format(s_code))
    else:
        print(r.text)
