#!/usr/bin/python3
def uppercase(s):
    result = ""
    diff = ord('a') - ord('A')
    for char in s:
        if 'a' <= char <= 'z':
            result += chr(ord(char) - diff)
        else:
            result += char

    print("{}".format(result))
