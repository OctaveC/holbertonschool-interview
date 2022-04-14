#!/usr/bin/python3
"""
Returns a list of lists of integers representing a Pascal’s triangle
"""


def pascal_triangle(n):
    """
    Returns a list of lists representing a Pascal's triangle
    """

    triangle = [[1]]
    if n == 1:
        return triangle

    triangle = []
    for ite1 in range(n):
        basis = [1]
        for ite2 in range(ite1):
            basis.append(sum(triangle[-1][ite2:ite2+2]))
        triangle.append(basis)
    return triangle
