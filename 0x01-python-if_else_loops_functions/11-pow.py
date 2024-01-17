#!/usr/bin/python3
def pow(a, b):
    result = 1
    
    # If b is negative, calculate reciprocal of a raised to abs(b)
    if b < 0:
        a = 1 / a
        b = abs(b)
    
    # Calculate a^b using a loop
    for _ in range(b):
        result *= a
        return round(result, 2)
