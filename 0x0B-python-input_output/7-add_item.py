#!/usr/bin/python3
"""Adds command-line arguments to a list and saves it to a JSON file."""

import sys

load_from_json_file = __import__('6-load_from_json_file').load_from_json_file
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file

def main():
    """Main function to add command-line arguments to a list and save to a file."""
    filename = 'add_item.json'

    # Load existing data from the file, or start with an empty list if the file doesn't exist
    try:
        data_list = load_from_json_file(filename)
    except FileNotFoundError:
        data_list = []

    # Append the command-line arguments to the list
    data_list.extend(sys.argv[1:])

    # Save the updated list to the file
    save_to_json_file(data_list, filename)

if __name__ == '__main__':
    main()
