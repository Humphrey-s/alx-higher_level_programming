#!/usr/bin/python3
"""Script that adds arguments to a python list and saves to a file."""
import sys
save_tjson = __import__('5-save_to_json_file').save_to_json_file
load_fjson = __import__('6-load_from_json_file').load_from_json_file

dlist = []
for i in range(1, len(sys.argv)):
    dlist.append(sys.argv[i])

filename = "add_item.json"
save_tjson(dlist, filename)
