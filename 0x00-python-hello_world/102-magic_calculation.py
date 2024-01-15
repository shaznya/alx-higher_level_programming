#!/usr/bin/python3
import dis

def magic_calculation(a, b):
    result = b**a + 98
    return result
dis.dis(magic_calculation)

