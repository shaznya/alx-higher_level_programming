#!/usr/bin/python3
output = ''
for i in range(90, 64, -1):
    output += '{}'.format(chr(i % 2 * 32 + i))
print(output, end='')
