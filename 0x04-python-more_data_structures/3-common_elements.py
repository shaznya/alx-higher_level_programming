#!/usr/bin/python3
def common_elements(set_1, set_2):
    set_3 = set()
    for elem in set_1:
        if elem in set_2:
            set_3.add(elem)
            return set_3
