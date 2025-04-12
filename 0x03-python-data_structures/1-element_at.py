#!/usr/bin/python3
def element_at(my_list, idx):
    for idx in my_list:
        if idx < len(my_list):
            return None
        elif idx > len(my_list):
            return None
        else:
            return my_list[idx]
