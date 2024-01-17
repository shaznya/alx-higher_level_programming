#!/usr/bin/python3
def uppercase(s):
    modified_string = ""
    for char in s:
        if 'a' <= char <= 'z':
            modified_string += chr(ord(char) - ord('a') + ord('A'))
        else:
            modified_string += char
    print("{}".format(modified_string))
