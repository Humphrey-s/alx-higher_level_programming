#!/usr/bin/python3
#Python script that fetches https://alx-intranet.hbtn.io/status
from urllib import request

def main():

    with request.urlopen("https://alx-intranet.hbtn.io/status") as r:
        print("Body response:")
        content = r.read().decode("utf-8")
        print("\t- type: ".format(type(r.read())))
        print("\t- content: {}".format(r.read()))
        print("\t- utf-8 content: {}".format(content))

if __name__ == "__main__":
    main()
