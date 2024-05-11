#!/usr/bin/python3
output = ''
for i in range(ord('z'), ord('a') - 1, -1):
    output += '{}'.format(chr(i % 2 * 32 + i))
print(output, end='')
