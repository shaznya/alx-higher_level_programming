#!/usr/bin/python3
def append_write(filename="", text=""):
    """Appends a string to a text file (UTF8)."""
    with open(filename, 'a', encoding='utf-8') as file:
        return file.write(text)
