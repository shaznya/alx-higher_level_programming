#!/usr/bin/python3
"""Insert a line of text after each line containing a specific string in a file."""

def append_after(filename="", search_string="", new_string=""):
    """Insert a line of text after each line containing a specific string.

    Args:
        filename (str): The name of the file to modify.
        search_string (str): The string to search for in the file.
        new_string (str): The line of text to insert after each line containing the search_string.
    """
    # Read the contents of the file
    with open(filename, 'r', encoding='utf-8') as file:
        lines = file.readlines()
    
    # Modify the contents
    with open(filename, 'w', encoding='utf-8') as file:
        for line in lines:
            file.write(line)
            if search_string in line:
                file.write(new_string + '\n')

if __name__ == "__main__":
    # Example usage
    append_after("example.txt", "search_this", "new line after")
