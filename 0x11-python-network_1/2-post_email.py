#!/usr/bin/python3
"""Python script that takes in a URL and an email, sends a POST request to the passed URL with the email as a parameter, and displays the body of the response (decoded in utf-8)"""
import sys
import urllib
from urllib import request

def main():

    values = {"email": sys.argv[2]}

    data = urllib.parse.urlencode(values).encode("ascii")
    url = request.Request(sys.argv[1], data)

    with request.urlopen(url) as r:
        print(r.read().decode("utf-8"))

if __name__ == "__main__":
    main()
