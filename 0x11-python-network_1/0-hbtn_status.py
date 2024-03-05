#!/usr/bin/python3
#Python script that fetches https://alx-intranet.hbtn.io/status
from urllib import request

def main():

    url = request.Request("https://alx-intranet.hbtn.io/status")

    with request.urlopen(url) as r:

        b = r.read()
        print("Body response:$")
        print("\t- type: ".format(type(b)))
        print("\t- content: {}".format(b))
        print("\t- utf-8 content: {}".format(b.decode("utf-8")))

if __name__ == "__main__":
    main()
