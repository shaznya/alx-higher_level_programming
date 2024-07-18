#!/usr/bin/python3
def matrix_mul(m_a, m_b):
    """
    Multiplies two matrices m_a and m_b.

    Args:
        m_a (list of list of int or float): The first matrix.
        m_b (list of list of int or float): The second matrix.

    Returns:
        list of list of float: The resulting matrix product of m_a and m_b.

    Raises:
        TypeError: If m_a or m_b is not a list or not a list of lists, or contains non-integer/float elements.
        ValueError: If m_a or m_b is empty, or if matrices cannot be multiplied due to incompatible dimensions.
    """
    # Validate m_a
    if not isinstance(m_a, list) or not all(isinstance(row, list) for row in m_a):
        raise TypeError("m_a must be a list of lists")
    if not m_a or any(not isinstance(num, (int, float)) for row in m_a for num in row):
        raise ValueError("m_a can't be empty and should contain only integers or floats")
    if any(len(row) != len(m_a[0]) for row in m_a):
        raise TypeError("each row of m_a must be of the same size")

    # Validate m_b
    if not isinstance(m_b, list) or not all(isinstance(row, list) for row in m_b):
        raise TypeError("m_b must be a list of lists")
    if not m_b or any(not isinstance(num, (int, float)) for row in m_b for num in row):
        raise ValueError("m_b can't be empty and should contain only integers or floats")
    if any(len(row) != len(m_b[0]) for row in m_b):
        raise TypeError("each row of m_b must be of the same size")

    # Validate multiplication compatibility
    if len(m_a[0]) != len(m_b):
        raise ValueError("m_a and m_b can't be multiplied")

    # Perform matrix multiplication
    rows_a = len(m_a)
    cols_a = len(m_a[0])
    cols_b = len(m_b[0])

    result = [[0 for _ in range(cols_b)] for _ in range(rows_a)]

    for i in range(rows_a):
        for j in range(cols_b):
            for k in range(cols_a):
                result[i][j] += m_a[i][k] * m_b[k][j]

    return result
