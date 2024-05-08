#!/usr/bin/python3
output = ''
for i in range(ord('z'), ord('a') - 1, -1):
    output += '{}'.format(chr(i).upper() if i % 2 == 0 else chr(i).lower())
print(output, end='')
