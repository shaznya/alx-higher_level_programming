#!/usr/bin/python3
output = ''
for i in range(122, 96, -1):
    output += '{}'.format(chr(i % 26 + 65))
print(output, end='')
