#!/usr/bin/python3
def element_at(my_list, idx):
    for i, element in enumerate(my_list):
        if i == idx:
            return element
        return idx < 0 or idx >= len(my_list)
