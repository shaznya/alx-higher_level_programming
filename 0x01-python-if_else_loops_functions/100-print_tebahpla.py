#!/usr/bin/python3
output = ''
for i in range(ord('z'), ord('a') - 1, -1):
    output += '{}'.format(chr(i).lower() if (ord('z') - i) % 2 == 0 else chr(i).upper())
    print(output, end='')
