#!/usr/bin/python3
if __name__ == "__main__":
    import sys

    argc = len(sys.argv) - 1
    plural_s = "s" if argc != 1 else ""
    period = "." if argc == 0 else ":"

    print(f"{argc} argument{plural_s}{period}")

    for i in range(1, argc + 1):
        print(f"{i}: {sys.argv[i]}")
