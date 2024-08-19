#!/usr/bin/python3
"""Inserts a line of text to a file after each line."""


def append_after(filename="", search_string="", new_string=""):
    """Appends `new_string` after every line."""
    lines = []
    with open(filename, 'r', encoding='utf-8') as file:
        for line in file:
            lines.append(line)
            if search_string in line:
                lines.append(new_string)

    with open(filename, 'w', encoding='utf-8') as file:
        file.writelines(lines)


if __name__ == "__main__":
    # Example usage
    append_after(
        "append_after_100.txt",
        "Python",
        "\"C is fun!\"\n"
    )
