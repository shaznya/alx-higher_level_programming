#!/usr/bin/python3
def uppercase(s):
    result = ""
    for char in s:
        diff = ord('a') - ord('A')
        upper_char = chr(ord(char) - diff) if 'a' <= char <= 'z' else char
        result += upper_char
    print("{}\n".format(result))
