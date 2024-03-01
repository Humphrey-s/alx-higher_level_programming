#!/usr/bin/python3
# Python script that takes in a URL, sends a request to the URL and displays the value of the X-Request-Id variable found in
from urllib import request
import sys


def main():
    url = sys.argv[1]

    with request.urlopen(url) as r:
        print(r.headers["X-Request-Id"])

if __name__ == "__main__":
    main()
