#!/usr/bin/python3
import numpy as np

def lazy_matrix_mul(m_a, m_b):
    """
    Multiplies two matrices m_a and m_b using NumPy.

    Args:
        m_a (list of list of int or float): The first matrix.
        m_b (list of list of int or float): The second matrix.

    Returns:
        numpy.ndarray: The resulting matrix product of m_a and m_b.

    Raises:
        TypeError: If m_a or m_b is not a list or not a list of lists, or contains non-integer/float elements.
        ValueError: If m_a or m_b is empty, or if matrices cannot be multiplied due to incompatible dimensions.
    """
    # Convert lists to NumPy arrays
    np_a = np.array(m_a, dtype=np.float64)
    np_b = np.array(m_b, dtype=np.float64)

    # Validate input matrices
    if not isinstance(m_a, list) or not all(isinstance(row, list) for row in m_a):
        raise TypeError("m_a must be a list of lists")
    if not m_a or any(not isinstance(num, (int, float)) for row in m_a for num in row):
        raise ValueError("m_a can't be empty and should contain only integers or floats")
    if any(len(row) != len(m_a[0]) for row in m_a):
        raise TypeError("each row of m_a must be of the same size")

    if not isinstance(m_b, list) or not all(isinstance(row, list) for row in m_b):
        raise TypeError("m_b must be a list of lists")
    if not m_b or any(not isinstance(num, (int, float)) for row in m_b for num in row):
        raise ValueError("m_b can't be empty and should contain only integers or floats")
    if any(len(row) != len(m_b[0]) for row in m_b):
        raise TypeError("each row of m_b must be of the same size")

    # Validate multiplication compatibility
    if len(m_a[0]) != len(m_b):
        raise ValueError("m_a and m_b can't be multiplied")

    # Perform matrix multiplication using NumPy
    result = np.dot(np_a, np_b)

    return result
