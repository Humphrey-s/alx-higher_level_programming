#!/usr/bin/python3
"""adds all arguments in a list and saves them to a file"""
import sys
import os
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file


if (os.path.exists("./add_item.json") == 0):

    ls_t = []
elif (os.path.getsize("./add_item.json") == 0):

    ls_t = []
else:
    ls_t = load_from_json_file("add_item.json")

n = len(sys.argv)


for i in range(1, n):

    ls_t.append(sys.argv[i])

save_to_json_file(ls_t, "./add_item.json")
