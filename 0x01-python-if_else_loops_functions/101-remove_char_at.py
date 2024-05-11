#!/usr/bin/python3
def remove_char_at(s, n):
    if n < 0 or n >= len(s):
        return s
    return ''.join([s[i] for i in range(len(s)) if i != n])
