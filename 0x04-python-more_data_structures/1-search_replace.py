#!/usr/bin/python3
def search_replace(my_list, search, replace):
    new_list = list(map(lambda t: replace if t[1] == search else t[1], enumerate(my_list)))
    return new_list
