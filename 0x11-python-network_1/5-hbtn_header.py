#!/usr/bin/python3
"""Sends a request to the URL and displays value of variable X-Request-Id"""
import requests
import sys


if __name__ == "__main__":

    res = requests.get(sys.argv[1])
    print(res.headers.get("X-Request-Id"))
