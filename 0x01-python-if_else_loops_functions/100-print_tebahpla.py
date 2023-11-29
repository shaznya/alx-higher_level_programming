#!/usr/bin/python3

for char_code in range(ord('z'), ord('a') - 1, -1):
    print("{}{}".format(chr(char_code), chr(char_code - 32) if char_code % 2 == 1 and char_code != ord('a') else ''), end='')
