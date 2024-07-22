#!/usr/bin/python3
"""
Module to multiply two matrices.
"""

def matrix_mul(m_a, m_b):
    """
    Multiplies two matrices.

    Args:
        m_a (list of lists of integers/floats): The first matrix.
        m_b (list of lists of integers/floats): The second matrix.

    Returns:
        list of lists of floats: The product matrix.

    Raises:
        TypeError: If m_a or m_b is not a list or if they are not lists of lists
                   or if they contain non-integer/float elements or if rows are not of same size.
        ValueError: If m_a or m_b is empty or if the matrices cannot be multiplied.
    """
    if not isinstance(m_a, list) or not all(isinstance(row, list) for row in m_a):
        raise TypeError("m_a must be a list of lists")
    if not isinstance(m_b, list) or not all(isinstance(row, list) for row in m_b):
        raise TypeError("m_b must be a list of lists")
    
    if not m_a or not m_a[0]:
        raise ValueError("m_a can't be empty")
    if not m_b or not m_b[0]:
        raise ValueError("m_b can't be empty")
    
    if not all(isinstance(element, (int, float)) for row in m_a for element in row):
        raise TypeError("m_a should contain only integers or floats")
    if not all(isinstance(element, (int, float)) for row in m_b for element in row):
        raise TypeError("m_b should contain only integers or floats")
    
    row_len_a = len(m_a[0])
    if not all(len(row) == row_len_a for row in m_a):
        raise TypeError("each row of m_a must be of the same size")
    
    row_len_b = len(m_b[0])
    if not all(len(row) == row_len_b for row in m_b):
        raise TypeError("each row of m_b must be of the same size")
    
    if len(m_a[0]) != len(m_b):
        raise ValueError("m_a and m_b can't be multiplied")

    # Perform matrix multiplication
    result = []
    for row in m_a:
        result_row = []
        for col in range(len(m_b[0])):
            result_row.append(sum(row[i] * m_b[i][col] for i in range(len(m_b))))
        result.append(result_row)

    return result
