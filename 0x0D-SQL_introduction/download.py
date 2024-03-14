#!/usr/bin/python3
import requests


p = requests.get("https://s3.amazonaws.com/intranet-projects-files/holbertonschool-higher-level_programming+/272/temperatures.sql")

with open("./temperatures.sql", "w") as f:
    f.write(p.text)
