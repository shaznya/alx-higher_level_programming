#!/usr/bin/python3
def remove_char_at(my_str, n):
    if n < 0 or n >= len(my_str):
        return my_str

    result = ""
    for i in range(len(my_str)):
        if i != n:
            result += my_str[i]

    return result
