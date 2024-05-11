#!/usr/bin/python3
for i in range(122, 96, -1):
    char = "{:c}".format(i)
    print(char if (122 - i) % 2 == 0 else char.upper(), end="")
