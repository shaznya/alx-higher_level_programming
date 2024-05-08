#!/usr/bin/python3
#!/usr/bin/python3
for c in range(ord('z'), ord('A') - 1, -1):
    print("{:c}".format(c if c % 2 == 1 else c - 32), end="")
