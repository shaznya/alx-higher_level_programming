#!/usr/bin/python3
"""Adds command-line arguments to a list and saves it to a JSON file."""

import sys
from load_from_json_file import load_from_json_file
from save_to_json_file import save_to_json_file


def main():
    """Main function to add command-line arguments."""
    filename = 'add_item.json'

    # Load existing data from the file
    try:
        data_list = load_from_json_file(filename)
    except FileNotFoundError:
        data_list = []

    # Append the command-line arguments to the list
    # sys.argv[0] is the script name, so we start from sys.argv[1]
    data_list.extend(sys.argv[1:])

    # Save the updated list to the file
    save_to_json_file(data_list, filename)


if __name__ == '__main__':
    main()
