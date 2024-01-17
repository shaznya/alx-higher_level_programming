#!/usr/bin/python3
def pow(a, b, precision=10):
    result = 1
    if b < 0:
        a = 1 / a
        b = -
    for _ in range(b):
        result *= a

    return round(result, precision
