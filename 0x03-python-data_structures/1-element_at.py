#!/usr/bin/python3
def element_at(my_list, idx):
    for i, value in enumerate(my_list):
        if i == idx:
            return value
    return None
