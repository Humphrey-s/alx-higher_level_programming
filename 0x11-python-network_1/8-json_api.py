#!/usr/bin/python3
"""Sends a POST request to url with letter as <param>"""
import sys
import requests


if __name__ == "__main__":

    if len(sys.argv) < 1:
        payload = {"q": ""}
    else:
        payload = {"q": sys.argv[1]}

    try:
        res = requests.post("http://0.0.0.0:5000/search_user", data=payload).json()

        if res == {}:
            print("No result")
        else:
            print("[{}] {}".format(res.get("id"), res.get("name")))

    except Exception as e:
        print("Not a valid JSON")
