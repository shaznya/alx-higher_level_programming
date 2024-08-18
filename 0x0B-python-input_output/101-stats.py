#!/usr/bin/python3
"""
Script that reads stdin line by line and computes metrics.

Input format: <IP Address> - [<date>] "GET /projects/260 HTTP/1.1" <status code> <file size>
Each 10 lines and after a keyboard interruption (CTRL + C), prints those statistics since the beginning:
    - Total file size: sum of all previous file sizes
    - Number of lines by status code in ascending order
"""

import sys

def print_stats(total_size, status_counts):
    """Prints the accumulated metrics."""
    print("File size: {}".format(total_size))
    for code in sorted(status_counts):
        if status_counts[code] > 0:
            print("{}: {}".format(code, status_counts[code]))

def main():
    total_size = 0
    status_counts = {200: 0, 301: 0, 400: 0, 401: 0, 403: 0, 404: 0, 405: 0, 500: 0}
    line_count = 0

    try:
        for line in sys.stdin:
            line_count += 1
            parts = line.split()
            try:
                # Extracting the status code and file size from the line
                status_code = int(parts[-2])
                file_size = int(parts[-1])
                total_size += file_size

                # Count the status code if it is one of the expected values
                if status_code in status_counts:
                    status_counts[status_code] += 1
            except (IndexError, ValueError):
                pass

            # Print stats every 10 lines
            if line_count % 10 == 0:
                print_stats(total_size, status_counts)

    except KeyboardInterrupt:
        print_stats(total_size, status_counts)
        raise

    # Print final stats after processing all lines
    print_stats(total_size, status_counts)

if __name__ == '__main__':
    main()
