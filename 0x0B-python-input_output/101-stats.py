#!/usr/bin/python3
"""Reads stdin line by line and computes metrics."""


def print_stats(total_size, status_codes):
    """Prints accumulated metrics."""
    print("File size: {}".format(total_size))
    for code in sorted(status_codes):
        if status_codes[code] > 0:
            print("{}: {}".format(code, status_codes[code]))


if __name__ == "__main__":
    import sys

    total_size = 0
    status_codes = {200: 0, 301: 0, 400: 0, 401: 0,
                    403: 0, 404: 0, 405: 0, 500: 0}
    count = 0

    try:
        for line in sys.stdin:
            count += 1
            parts = line.split()

            try:
                total_size += int(parts[-1])
                code = int(parts[-2])
                if code in status_codes:
                    status_codes[code] += 1
            except (IndexError, ValueError):
                pass

            if count % 10 == 0:
                print_stats(total_size, status_codes)

    except KeyboardInterrupt:
        print_stats(total_size, status_codes)
        raise

    print_stats(total_size, status_codes)
