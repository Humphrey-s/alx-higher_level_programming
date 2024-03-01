#!/usr/bin/python3
#Python script that fetches https://alx-intranet.hbtn.io/status
from urllib import request

def main():

    with request.urlopen("https://alx-intranet.hbtn.io/status") as r:
        content = r.read()
        print(content)

if __name__ == "__main__":
    main()
