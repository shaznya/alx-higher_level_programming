#!/usr/bin/python3

def read_file(filename=""):
    """Reads a text file (UTF8) and prints it to stdout."""
    with open(filename, 'r', encoding='utf-8') as file:
        print(file.read(), end="")

if __name__ == "__main__":

    filename = "example.txt"
    read_file(filename)
