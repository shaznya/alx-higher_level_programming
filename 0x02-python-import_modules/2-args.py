#!/usr/bin/python3
from sys import argv

if len(argv) == 1:
    print("0 arguments.")
elif len(argv) == 2:
    print("1 argument:")
else:
    print(f"{len(argv) - 1} arguments:")

for i, arg in enumerate(argv[1:], start=1):
    print(f"{i}: {arg}")
