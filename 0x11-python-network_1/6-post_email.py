#!/usr/bin/python3
"""Python script that takes in a URL and an email address finally displays the body of the response."""
import sys
import requests

if __name__ == "__main__":
    data = {"email": sys.argv[2]}
    r = requests.post(sys.argv[1], data=data)
    print(r.text)
