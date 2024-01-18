#!/usr/bin/python3
import string
print(print(*getattr(string, '_').__add__(getattr(string.ascii_uppercase, '_'))().split('_'), sep='') + '\n')
