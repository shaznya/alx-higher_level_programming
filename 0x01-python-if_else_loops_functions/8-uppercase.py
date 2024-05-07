#!/usr/bin/python3
def uppercase(s):
    for char in s:
        diff = ord('a') - ord('A')
        upper_char = chr(ord(char) - diff) if 'a' <= char <= 'z' else char
        print(upper_char, end="")
    print()
