#!/usr/bin/python3
def uppercase(str):
    for i in str(ord('A'), ord('Z') + 1):
        print("{}".format(chr(i)))
