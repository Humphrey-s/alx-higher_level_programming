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
            url = "http://0.0.0.0:5000/search_user"
            res = requests.post(url, data=payload).json()

            if res == {}:
                print("No result")
            else:
                print("[{}] {}".format(res.get("id"), res.get("name")))
        except ValueError:
            print("Not a valid JSON")
