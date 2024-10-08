#!/usr/bin/python3
"""Generate Pascal's Triangle of n rows."""


def pascal_triangle(n):
    """Generate Pascal's triangle of n rows.

    Args:
        n (int): The number of rows in Pascal's triangle.

        Returns:
        list: A list of lists representing Pascal's triangle.
    """
    if n <= 0:
        return []
    triangle = [[1]]

    for i in range(1, n):
        row = [1]
        for j in range(1, i):
            row.append(triangle[i-1][j-1] + triangle[i-1][j])
        row.append(1)
        triangle.append(row)

    return triangle


if __name__ == "__main__":
    n = 5
    result = pascal_triangle(n)
    for row in result:
        print(row)
