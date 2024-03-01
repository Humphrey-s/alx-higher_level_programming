#!/usr/bin/python3
#Python script that fetches https://alx-intranet.hbtn.io/status
from urllib import request

def main():

    with request.urlopen("https://alx-intranet.hbtn.io/status") as r:
        print("Body response:")
        print("\t- type: ".format(type(r.read())))
        content = r.read()
        print("\t- content: {}", content)

if __name__ == "__main__":
    main()
