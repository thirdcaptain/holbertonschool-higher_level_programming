#!/usr/bin/python3
"""
module defines script that adds all arguments to python list
"""


from sys import argv

save_to_json_file = __import__('7-save_to_json_file').save_to_json_file
load_from_json_file = __import__('8-load_from_json_file').load_from_json_file

json_list = list(argv[1:])
filename = "add_item.json"
save_to_json_file(json_list, filename)
