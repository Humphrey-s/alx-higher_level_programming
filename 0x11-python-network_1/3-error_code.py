#!/usr/bin/python3
""" Takes in a URL, sends a request to the URL and displays response"""
import sys
from urllib import request
import urllib.error


if __name__ == "__main__":

    try:
        url = request.Request(sys.argv[1])

        with request.urlopen(url) as r:
            print(r.read().decode("utf-8"))

    except urllib.error.HTTPError as e:
        p = e.code
        print("Error code: {}".format(p))
