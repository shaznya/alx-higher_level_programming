#!/usr/bin/python3
def remove_char_at(s, n):
    if n < 0 or n >= len(s):
        # If the index is out of bounds, return the original string
        return s
    
    # Create a new string by concatenating the substring before and after the specified index
    return s[:n] + s[n+1:]

# Example usage:
original_string = "Hello, World!"
index_to_remove = 7
result = remove_char_at(original_string, index_to_remove)
print(result)
