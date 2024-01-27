#!/usr/bin/python3
def uniq_add(my_list=[]):
    unique_set = set()

    for number in my_list:
        if isinstance(number, int):
            unique_set.add(number)

    return sum(unique_set)
