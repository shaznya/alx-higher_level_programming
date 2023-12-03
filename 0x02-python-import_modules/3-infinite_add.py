#!/usr/bin/python3
import sys

if __name__ == "__main__":

    arguments = sys.argv[1:]

    if arguments:

        result = sum(int(arg) for arg in arguments)

        print(result)

    else:
        print("0")
