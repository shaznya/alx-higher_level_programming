#!/usr/bin/python3
"""
Module to print text with 2 new lines after each of these characters: ., ? and :
"""

def text_indentation(text):
    """
    Prints a text with 2 new lines after each of the characters: ., ?, and :.
    
    Args:
        text (str): The text to be formatted.
        
    Raises:
        TypeError: If text is not a string.
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    
    formatted_text = ""
    i = 0

    while i < len(text):
        formatted_text += text[i]

        if text[i] in '.?:':
            if i + 1 < len(text) and text[i + 1] == ' ':
                i += 1
                formatted_text += '\n\n'
                while i < len(text) and text[i] == ' ':
                    i += 1
                continue
            else:
                formatted_text += '\n\n'
        
        i += 1
    print(formatted_text.strip())
