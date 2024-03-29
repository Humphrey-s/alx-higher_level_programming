#!/usr/bin/python3
"""Python script that fetches https://alx-intranet.hbtn.io/status"""
from urllib import request


if __name__ == "__main__":

    url = request.Request("https://alx-intranet.hbtn.io/status")

    with request.urlopen(url) as r:

        b = r.read()
        print("Body response:")
        print("\t- type: {}".format(type(b)))
        print("\t- content: {}".format(b))
        print("\t- utf8 content: {}".format(b.decode("utf-8")))
