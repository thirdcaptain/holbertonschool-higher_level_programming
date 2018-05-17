#!/usr/bin/python3
"""
module defines script that adds all arguments to python list
"""


from sys import argv

save_to_json_file = __import__('7-save_to_json_file').save_to_json_file
load_from_json_file = __import__('8-load_from_json_file').load_from_json_file

filename = "add_item.json"
json_list = argv[1:]
my_obj = load_from_json_file(filename)
my_obj += json_list
save_to_json_file(my_obj, filename)
