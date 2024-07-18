#!/usr/bin/python3
def text_indentation(text):
    """
    Prints text with 2 new lines after each '.', '?' and ':' characters.

    Args:
        text (str): The input text to be processed.

    Raises:
        TypeError: If text is not a string.
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    lines = []
    line = ""

    for char in text:
        line += char

        if char in ['.', '?', ':']:
            lines.append(line.strip())
            lines.append("")
            line = ""

    if line:
        lines.append(line.strip())

    for line in lines:
        print(line)
