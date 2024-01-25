#!/usr/bin/python3
def search_replace(my_list, search, replace):
    replace_func = lambda x: replace if x == search else x
    new_list = list(map(replace_func, my_list))
    return new_list
