#!/usr/bin/python3
""" Python script that takes in a URL, sends a request to the URL and displays the body of the response (decoded in utf-8)."""
import sys
from urllib import request


def main():

    with request.urlopen(sys.argv[1]) as r:
        try:
            print(r.read().decode("utf-8"))
        except urllib.error.HTTPError as e:
            p = e.code
            print("Error code: {}".format(p))

if __name__ == "__main__":
    main()
